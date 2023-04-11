
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: tstate_current_as_th
- machine: windows-amd64
- commit hash: 2332a2e
- commit date: 2023-04-07
- overall geometric mean: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 229 ms                                                                   | 210 ms: 1.09x faster                                                                   |
| chameleon      | 5.77 ms                                                                  | 4.55 ms: 1.27x faster                                                                  |
| docutils       | 1.83 sec                                                                 | 1.59 sec: 1.15x faster                                                                 |
| html5lib       | 47.3 ms                                                                  | 37.3 ms: 1.27x faster                                                                  |
| tornado_http   | 106 ms                                                                   | 90.5 ms: 1.18x faster                                                                  |
| Geometric mean | (ref)                                                                    | 1.19x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 71.5 ms                                                                  | 58.2 ms: 1.23x faster                                                                  |
| float          | 59.5 ms                                                                  | 48.8 ms: 1.22x faster                                                                  |
| pidigits       | 145 ms                                                                   | 151 ms: 1.04x slower                                                                   |
| Geometric mean | (ref)                                                                    | 1.13x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                                   | 83.0 ms: 1.25x faster                                                                  |
| regex_v8       | 15.1 ms                                                                  | 14.1 ms: 1.07x faster                                                                  |
| regex_dna      | 131 ms                                                                   | 123 ms: 1.06x faster                                                                   |
| Geometric mean | (ref)                                                                    | 1.09x faster                                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps           | 9.00 ms                                                                  | 5.61 ms: 1.60x faster                                                                  |
| pickle_pure_python   | 264 us                                                                   | 176 us: 1.50x faster                                                                   |
| unpickle_pure_python | 179 us                                                                   | 125 us: 1.43x faster                                                                   |
| xml_etree_process    | 43.0 ms                                                                  | 36.8 ms: 1.17x faster                                                                  |
| json_loads           | 14.2 us                                                                  | 13.0 us: 1.09x faster                                                                  |
| unpickle             | 8.88 us                                                                  | 8.44 us: 1.05x faster                                                                  |
| xml_etree_parse      | 95.6 ms                                                                  | 91.6 ms: 1.04x faster                                                                  |
| xml_etree_generate   | 53.8 ms                                                                  | 52.1 ms: 1.03x faster                                                                  |
| xml_etree_iterparse  | 62.5 ms                                                                  | 61.2 ms: 1.02x faster                                                                  |
| unpickle_list        | 2.71 us                                                                  | 2.85 us: 1.05x slower                                                                  |
| pickle               | 6.67 us                                                                  | 7.04 us: 1.06x slower                                                                  |
| pickle_list          | 2.57 us                                                                  | 2.83 us: 1.10x slower                                                                  |
| pickle_dict          | 16.7 us                                                                  | 18.9 us: 1.13x slower                                                                  |
| Geometric mean       | (ref)                                                                    | 1.11x faster                                                                           |

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
| mako            | 8.69 ms                                                                  | 6.23 ms: 1.39x faster                                                                  |
| genshi_text     | 18.5 ms                                                                  | 13.4 ms: 1.38x faster                                                                  |
| django_template | 29.2 ms                                                                  | 21.9 ms: 1.33x faster                                                                  |
| genshi_xml      | 38.8 ms                                                                  | 30.4 ms: 1.27x faster                                                                  |
| Geometric mean  | (ref)                                                                    | 1.34x faster                                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| deltablue               | 4.15 ms                                                                  | 2.00 ms: 2.07x faster                                                                  |
| go                      | 143 ms                                                                   | 84.3 ms: 1.70x faster                                                                  |
| logging_silent          | 94.6 ns                                                                  | 55.8 ns: 1.70x faster                                                                  |
| richards                | 41.0 ms                                                                  | 24.5 ms: 1.67x faster                                                                  |
| json_dumps              | 9.00 ms                                                                  | 5.61 ms: 1.60x faster                                                                  |
| sqlglot_parse           | 1.22 ms                                                                  | 763 us: 1.60x faster                                                                   |
| scimark_lu              | 83.9 ms                                                                  | 53.4 ms: 1.57x faster                                                                  |
| sqlglot_transpile       | 1.47 ms                                                                  | 952 us: 1.54x faster                                                                   |
| generators              | 31.4 ms                                                                  | 20.8 ms: 1.51x faster                                                                  |
| raytrace                | 267 ms                                                                   | 177 ms: 1.50x faster                                                                   |
| mypy2                   | 337 ms                                                                   | 224 ms: 1.50x faster                                                                   |
| pickle_pure_python      | 264 us                                                                   | 176 us: 1.50x faster                                                                   |
| unpack_sequence         | 39.4 ns                                                                  | 26.4 ns: 1.49x faster                                                                  |
| scimark_sor             | 104 ms                                                                   | 69.8 ms: 1.48x faster                                                                  |
| unpickle_pure_python    | 179 us                                                                   | 125 us: 1.43x faster                                                                   |
| hexiom                  | 5.45 ms                                                                  | 3.81 ms: 1.43x faster                                                                  |
| chaos                   | 58.4 ms                                                                  | 41.5 ms: 1.41x faster                                                                  |
| mako                    | 8.69 ms                                                                  | 6.23 ms: 1.39x faster                                                                  |
| pyflate                 | 388 ms                                                                   | 279 ms: 1.39x faster                                                                   |
| deepcopy_memo           | 28.4 us                                                                  | 20.5 us: 1.38x faster                                                                  |
| genshi_text             | 18.5 ms                                                                  | 13.4 ms: 1.38x faster                                                                  |
| asyncio_tcp             | 664 ms                                                                   | 492 ms: 1.35x faster                                                                   |
| scimark_monte_carlo     | 56.0 ms                                                                  | 41.6 ms: 1.35x faster                                                                  |
| async_tree_memoization  | 485 ms                                                                   | 360 ms: 1.35x faster                                                                   |
| django_template         | 29.2 ms                                                                  | 21.9 ms: 1.33x faster                                                                  |
| async_tree_none         | 414 ms                                                                   | 312 ms: 1.33x faster                                                                   |
| pycparser               | 873 ms                                                                   | 658 ms: 1.33x faster                                                                   |
| async_tree_io           | 1.02 sec                                                                 | 777 ms: 1.32x faster                                                                   |
| thrift                  | 632 us                                                                   | 482 us: 1.31x faster                                                                   |
| crypto_pyaes            | 61.4 ms                                                                  | 47.2 ms: 1.30x faster                                                                  |
| pprint_pformat          | 1.23 sec                                                                 | 951 ms: 1.29x faster                                                                   |
| spectral_norm           | 74.3 ms                                                                  | 57.9 ms: 1.28x faster                                                                  |
| genshi_xml              | 38.8 ms                                                                  | 30.4 ms: 1.27x faster                                                                  |
| chameleon               | 5.77 ms                                                                  | 4.55 ms: 1.27x faster                                                                  |
| html5lib                | 47.3 ms                                                                  | 37.3 ms: 1.27x faster                                                                  |
| pprint_safe_repr        | 593 ms                                                                   | 468 ms: 1.27x faster                                                                   |
| regex_compile           | 103 ms                                                                   | 83.0 ms: 1.25x faster                                                                  |
| async_tree_cpu_io_mixed | 604 ms                                                                   | 488 ms: 1.24x faster                                                                   |
| nbody                   | 71.5 ms                                                                  | 58.2 ms: 1.23x faster                                                                  |
| float                   | 59.5 ms                                                                  | 48.8 ms: 1.22x faster                                                                  |
| scimark_sparse_mat_mult | 2.67 ms                                                                  | 2.21 ms: 1.21x faster                                                                  |
| sqlglot_optimize        | 38.7 ms                                                                  | 32.3 ms: 1.20x faster                                                                  |
| scimark_fft             | 187 ms                                                                   | 159 ms: 1.18x faster                                                                   |
| tornado_http            | 106 ms                                                                   | 90.5 ms: 1.18x faster                                                                  |
| deepcopy                | 256 us                                                                   | 218 us: 1.17x faster                                                                   |
| xml_etree_process       | 43.0 ms                                                                  | 36.8 ms: 1.17x faster                                                                  |
| sqlglot_normalize       | 201 ms                                                                   | 173 ms: 1.16x faster                                                                   |
| docutils                | 1.83 sec                                                                 | 1.59 sec: 1.15x faster                                                                 |
| deepcopy_reduce         | 2.18 us                                                                  | 1.90 us: 1.15x faster                                                                  |
| json                    | 3.18 ms                                                                  | 2.80 ms: 1.13x faster                                                                  |
| bench_thread_pool       | 953 us                                                                   | 852 us: 1.12x faster                                                                   |
| sqlite_synth            | 1.85 us                                                                  | 1.66 us: 1.11x faster                                                                  |
| mdp                     | 1.60 sec                                                                 | 1.46 sec: 1.10x faster                                                                 |
| sympy_expand            | 313 ms                                                                   | 286 ms: 1.09x faster                                                                   |
| dulwich_log             | 47.0 ms                                                                  | 43.0 ms: 1.09x faster                                                                  |
| 2to3                    | 229 ms                                                                   | 210 ms: 1.09x faster                                                                   |
| comprehensions          | 16.0 us                                                                  | 14.6 us: 1.09x faster                                                                  |
| json_loads              | 14.2 us                                                                  | 13.0 us: 1.09x faster                                                                  |
| nqueens                 | 64.8 ms                                                                  | 59.5 ms: 1.09x faster                                                                  |
| sympy_integrate         | 14.7 ms                                                                  | 13.7 ms: 1.07x faster                                                                  |
| regex_v8                | 15.1 ms                                                                  | 14.1 ms: 1.07x faster                                                                  |
| create_gc_cycles        | 764 us                                                                   | 718 us: 1.06x faster                                                                   |
| coroutines              | 15.6 ms                                                                  | 14.7 ms: 1.06x faster                                                                  |
| regex_dna               | 131 ms                                                                   | 123 ms: 1.06x faster                                                                   |
| fannkuch                | 252 ms                                                                   | 239 ms: 1.05x faster                                                                   |
| unpickle                | 8.88 us                                                                  | 8.44 us: 1.05x faster                                                                  |
| xml_etree_parse         | 95.6 ms                                                                  | 91.6 ms: 1.04x faster                                                                  |
| sympy_str               | 189 ms                                                                   | 183 ms: 1.03x faster                                                                   |
| xml_etree_generate      | 53.8 ms                                                                  | 52.1 ms: 1.03x faster                                                                  |
| xml_etree_iterparse     | 62.5 ms                                                                  | 61.2 ms: 1.02x faster                                                                  |
| python_startup          | 19.3 ms                                                                  | 19.0 ms: 1.02x faster                                                                  |
| meteor_contest          | 74.3 ms                                                                  | 73.4 ms: 1.01x faster                                                                  |
| pidigits                | 145 ms                                                                   | 151 ms: 1.04x slower                                                                   |
| logging_simple          | 6.12 us                                                                  | 6.39 us: 1.04x slower                                                                  |
| unpickle_list           | 2.71 us                                                                  | 2.85 us: 1.05x slower                                                                  |
| pickle                  | 6.67 us                                                                  | 7.04 us: 1.06x slower                                                                  |
| async_generators        | 214 ms                                                                   | 227 ms: 1.06x slower                                                                   |
| python_startup_no_site  | 14.8 ms                                                                  | 16.0 ms: 1.08x slower                                                                  |
| pickle_list             | 2.57 us                                                                  | 2.83 us: 1.10x slower                                                                  |
| pathlib                 | 75.2 ms                                                                  | 84.4 ms: 1.12x slower                                                                  |
| pickle_dict             | 16.7 us                                                                  | 18.9 us: 1.13x slower                                                                  |
| gc_traversal            | 1.33 ms                                                                  | 1.51 ms: 1.14x slower                                                                  |
| bench_mp_pool           | 59.2 ms                                                                  | 67.7 ms: 1.14x slower                                                                  |
| dask                    | 310 ms                                                                   | 359 ms: 1.16x slower                                                                   |
| coverage                | 37.5 ms                                                                  | 53.2 ms: 1.42x slower                                                                  |
| Geometric mean          | (ref)                                                                    | 1.19x faster                                                                           |

Benchmark hidden because not significant (4): regex_effbot, telco, sympy_sum, logging_format
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
