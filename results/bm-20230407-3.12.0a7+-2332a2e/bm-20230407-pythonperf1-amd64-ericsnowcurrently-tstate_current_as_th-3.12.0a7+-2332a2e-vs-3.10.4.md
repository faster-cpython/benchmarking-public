
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: tstate_current_as_th
- machine: windows-amd64
- commit hash: 2332a2e
- commit date: 2023-04-07
- overall geometric mean: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 229 ms                                                                   | 209 ms: 1.10x faster                                                                   |
| chameleon      | 5.77 ms                                                                  | 4.71 ms: 1.23x faster                                                                  |
| docutils       | 1.83 sec                                                                 | 1.60 sec: 1.14x faster                                                                 |
| html5lib       | 47.3 ms                                                                  | 37.4 ms: 1.27x faster                                                                  |
| tornado_http   | 106 ms                                                                   | 86.8 ms: 1.23x faster                                                                  |
| Geometric mean | (ref)                                                                    | 1.19x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 59.5 ms                                                                  | 50.2 ms: 1.18x faster                                                                  |
| nbody          | 71.5 ms                                                                  | 62.0 ms: 1.15x faster                                                                  |
| pidigits       | 145 ms                                                                   | 146 ms: 1.01x slower                                                                   |
| Geometric mean | (ref)                                                                    | 1.11x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                                   | 86.5 ms: 1.20x faster                                                                  |
| regex_dna      | 131 ms                                                                   | 120 ms: 1.09x faster                                                                   |
| regex_v8       | 15.1 ms                                                                  | 14.1 ms: 1.07x faster                                                                  |
| regex_effbot   | 1.64 ms                                                                  | 1.54 ms: 1.06x faster                                                                  |
| Geometric mean | (ref)                                                                    | 1.10x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps           | 9.00 ms                                                                  | 5.51 ms: 1.63x faster                                                                  |
| pickle_pure_python   | 264 us                                                                   | 182 us: 1.45x faster                                                                   |
| unpickle_pure_python | 179 us                                                                   | 129 us: 1.39x faster                                                                   |
| xml_etree_process    | 43.0 ms                                                                  | 36.3 ms: 1.18x faster                                                                  |
| json_loads           | 14.2 us                                                                  | 13.1 us: 1.08x faster                                                                  |
| unpickle             | 8.88 us                                                                  | 8.43 us: 1.05x faster                                                                  |
| xml_etree_generate   | 53.8 ms                                                                  | 52.8 ms: 1.02x faster                                                                  |
| xml_etree_parse      | 95.6 ms                                                                  | 94.2 ms: 1.01x faster                                                                  |
| unpickle_list        | 2.71 us                                                                  | 2.82 us: 1.04x slower                                                                  |
| xml_etree_iterparse  | 62.5 ms                                                                  | 65.3 ms: 1.04x slower                                                                  |
| pickle               | 6.67 us                                                                  | 7.39 us: 1.11x slower                                                                  |
| pickle_list          | 2.57 us                                                                  | 2.93 us: 1.14x slower                                                                  |
| pickle_dict          | 16.7 us                                                                  | 19.6 us: 1.18x slower                                                                  |
| Geometric mean       | (ref)                                                                    | 1.08x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 19.3 ms                                                                  | 19.0 ms: 1.02x faster                                                                  |
| python_startup_no_site | 14.8 ms                                                                  | 16.0 ms: 1.08x slower                                                                  |
| Geometric mean         | (ref)                                                                    | 1.03x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako            | 8.69 ms                                                                  | 6.38 ms: 1.36x faster                                                                  |
| django_template | 29.2 ms                                                                  | 22.0 ms: 1.32x faster                                                                  |
| genshi_text     | 18.5 ms                                                                  | 14.2 ms: 1.31x faster                                                                  |
| genshi_xml      | 38.8 ms                                                                  | 31.1 ms: 1.25x faster                                                                  |
| Geometric mean  | (ref)                                                                    | 1.31x faster                                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| deltablue               | 4.15 ms                                                                  | 2.01 ms: 2.07x faster                                                                  |
| go                      | 143 ms                                                                   | 86.3 ms: 1.66x faster                                                                  |
| logging_silent          | 94.6 ns                                                                  | 57.6 ns: 1.64x faster                                                                  |
| json_dumps              | 9.00 ms                                                                  | 5.51 ms: 1.63x faster                                                                  |
| sqlglot_parse           | 1.22 ms                                                                  | 757 us: 1.61x faster                                                                   |
| richards                | 41.0 ms                                                                  | 26.8 ms: 1.53x faster                                                                  |
| sqlglot_transpile       | 1.47 ms                                                                  | 974 us: 1.51x faster                                                                   |
| scimark_lu              | 83.9 ms                                                                  | 55.6 ms: 1.51x faster                                                                  |
| mypy2                   | 337 ms                                                                   | 225 ms: 1.50x faster                                                                   |
| generators              | 31.4 ms                                                                  | 21.5 ms: 1.46x faster                                                                  |
| raytrace                | 267 ms                                                                   | 184 ms: 1.45x faster                                                                   |
| pickle_pure_python      | 264 us                                                                   | 182 us: 1.45x faster                                                                   |
| unpack_sequence         | 39.4 ns                                                                  | 27.3 ns: 1.44x faster                                                                  |
| unpickle_pure_python    | 179 us                                                                   | 129 us: 1.39x faster                                                                   |
| crypto_pyaes            | 61.4 ms                                                                  | 45.0 ms: 1.36x faster                                                                  |
| mako                    | 8.69 ms                                                                  | 6.38 ms: 1.36x faster                                                                  |
| asyncio_tcp             | 664 ms                                                                   | 489 ms: 1.36x faster                                                                   |
| scimark_sor             | 104 ms                                                                   | 76.6 ms: 1.35x faster                                                                  |
| hexiom                  | 5.45 ms                                                                  | 4.06 ms: 1.34x faster                                                                  |
| scimark_monte_carlo     | 56.0 ms                                                                  | 41.9 ms: 1.34x faster                                                                  |
| pyflate                 | 388 ms                                                                   | 291 ms: 1.33x faster                                                                   |
| async_tree_memoization  | 485 ms                                                                   | 365 ms: 1.33x faster                                                                   |
| chaos                   | 58.4 ms                                                                  | 44.1 ms: 1.33x faster                                                                  |
| django_template         | 29.2 ms                                                                  | 22.0 ms: 1.32x faster                                                                  |
| async_tree_io           | 1.02 sec                                                                 | 778 ms: 1.32x faster                                                                   |
| genshi_text             | 18.5 ms                                                                  | 14.2 ms: 1.31x faster                                                                  |
| async_tree_none         | 414 ms                                                                   | 317 ms: 1.31x faster                                                                   |
| pycparser               | 873 ms                                                                   | 670 ms: 1.30x faster                                                                   |
| thrift                  | 632 us                                                                   | 488 us: 1.30x faster                                                                   |
| deepcopy_memo           | 28.4 us                                                                  | 22.4 us: 1.27x faster                                                                  |
| html5lib                | 47.3 ms                                                                  | 37.4 ms: 1.27x faster                                                                  |
| pprint_pformat          | 1.23 sec                                                                 | 973 ms: 1.26x faster                                                                   |
| async_tree_cpu_io_mixed | 604 ms                                                                   | 482 ms: 1.25x faster                                                                   |
| genshi_xml              | 38.8 ms                                                                  | 31.1 ms: 1.25x faster                                                                  |
| spectral_norm           | 74.3 ms                                                                  | 59.5 ms: 1.25x faster                                                                  |
| pprint_safe_repr        | 593 ms                                                                   | 479 ms: 1.24x faster                                                                   |
| chameleon               | 5.77 ms                                                                  | 4.71 ms: 1.23x faster                                                                  |
| tornado_http            | 106 ms                                                                   | 86.8 ms: 1.23x faster                                                                  |
| regex_compile           | 103 ms                                                                   | 86.5 ms: 1.20x faster                                                                  |
| sqlglot_optimize        | 38.7 ms                                                                  | 32.5 ms: 1.19x faster                                                                  |
| float                   | 59.5 ms                                                                  | 50.2 ms: 1.18x faster                                                                  |
| xml_etree_process       | 43.0 ms                                                                  | 36.3 ms: 1.18x faster                                                                  |
| scimark_sparse_mat_mult | 2.67 ms                                                                  | 2.28 ms: 1.17x faster                                                                  |
| json                    | 3.18 ms                                                                  | 2.73 ms: 1.16x faster                                                                  |
| mdp                     | 1.60 sec                                                                 | 1.39 sec: 1.15x faster                                                                 |
| nbody                   | 71.5 ms                                                                  | 62.0 ms: 1.15x faster                                                                  |
| docutils                | 1.83 sec                                                                 | 1.60 sec: 1.14x faster                                                                 |
| sqlglot_normalize       | 201 ms                                                                   | 178 ms: 1.13x faster                                                                   |
| deepcopy                | 256 us                                                                   | 229 us: 1.12x faster                                                                   |
| scimark_fft             | 187 ms                                                                   | 169 ms: 1.11x faster                                                                   |
| bench_thread_pool       | 953 us                                                                   | 861 us: 1.11x faster                                                                   |
| create_gc_cycles        | 764 us                                                                   | 692 us: 1.11x faster                                                                   |
| sympy_expand            | 313 ms                                                                   | 283 ms: 1.11x faster                                                                   |
| 2to3                    | 229 ms                                                                   | 209 ms: 1.10x faster                                                                   |
| regex_dna               | 131 ms                                                                   | 120 ms: 1.09x faster                                                                   |
| nqueens                 | 64.8 ms                                                                  | 59.9 ms: 1.08x faster                                                                  |
| sympy_integrate         | 14.7 ms                                                                  | 13.6 ms: 1.08x faster                                                                  |
| json_loads              | 14.2 us                                                                  | 13.1 us: 1.08x faster                                                                  |
| deepcopy_reduce         | 2.18 us                                                                  | 2.02 us: 1.08x faster                                                                  |
| dulwich_log             | 47.0 ms                                                                  | 43.6 ms: 1.08x faster                                                                  |
| regex_v8                | 15.1 ms                                                                  | 14.1 ms: 1.07x faster                                                                  |
| sqlite_synth            | 1.85 us                                                                  | 1.73 us: 1.06x faster                                                                  |
| regex_effbot            | 1.64 ms                                                                  | 1.54 ms: 1.06x faster                                                                  |
| comprehensions          | 16.0 us                                                                  | 15.1 us: 1.06x faster                                                                  |
| sympy_str               | 189 ms                                                                   | 178 ms: 1.06x faster                                                                   |
| unpickle                | 8.88 us                                                                  | 8.43 us: 1.05x faster                                                                  |
| xml_etree_generate      | 53.8 ms                                                                  | 52.8 ms: 1.02x faster                                                                  |
| python_startup          | 19.3 ms                                                                  | 19.0 ms: 1.02x faster                                                                  |
| xml_etree_parse         | 95.6 ms                                                                  | 94.2 ms: 1.01x faster                                                                  |
| coroutines              | 15.6 ms                                                                  | 15.4 ms: 1.01x faster                                                                  |
| sympy_sum               | 102 ms                                                                   | 101 ms: 1.01x faster                                                                   |
| pidigits                | 145 ms                                                                   | 146 ms: 1.01x slower                                                                   |
| logging_format          | 6.53 us                                                                  | 6.63 us: 1.01x slower                                                                  |
| logging_simple          | 6.12 us                                                                  | 6.25 us: 1.02x slower                                                                  |
| telco                   | 3.77 ms                                                                  | 3.88 ms: 1.03x slower                                                                  |
| async_generators        | 214 ms                                                                   | 221 ms: 1.03x slower                                                                   |
| unpickle_list           | 2.71 us                                                                  | 2.82 us: 1.04x slower                                                                  |
| xml_etree_iterparse     | 62.5 ms                                                                  | 65.3 ms: 1.04x slower                                                                  |
| python_startup_no_site  | 14.8 ms                                                                  | 16.0 ms: 1.08x slower                                                                  |
| pickle                  | 6.67 us                                                                  | 7.39 us: 1.11x slower                                                                  |
| gc_traversal            | 1.33 ms                                                                  | 1.49 ms: 1.12x slower                                                                  |
| pickle_list             | 2.57 us                                                                  | 2.93 us: 1.14x slower                                                                  |
| bench_mp_pool           | 59.2 ms                                                                  | 67.6 ms: 1.14x slower                                                                  |
| dask                    | 310 ms                                                                   | 364 ms: 1.17x slower                                                                   |
| pickle_dict             | 16.7 us                                                                  | 19.6 us: 1.18x slower                                                                  |
| pathlib                 | 75.2 ms                                                                  | 88.8 ms: 1.18x slower                                                                  |
| coverage                | 37.5 ms                                                                  | 52.7 ms: 1.41x slower                                                                  |
| Geometric mean          | (ref)                                                                    | 1.17x faster                                                                           |

Benchmark hidden because not significant (2): fannkuch, meteor_contest
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
