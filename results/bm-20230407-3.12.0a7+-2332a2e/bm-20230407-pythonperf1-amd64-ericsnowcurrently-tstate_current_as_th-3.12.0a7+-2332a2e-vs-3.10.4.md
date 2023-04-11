
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
| 2to3           | 229 ms                                                                   | 210 ms: 1.09x faster                                                                   |
| chameleon      | 5.77 ms                                                                  | 4.66 ms: 1.24x faster                                                                  |
| docutils       | 1.83 sec                                                                 | 1.60 sec: 1.15x faster                                                                 |
| html5lib       | 47.3 ms                                                                  | 37.7 ms: 1.26x faster                                                                  |
| tornado_http   | 106 ms                                                                   | 90.7 ms: 1.17x faster                                                                  |
| Geometric mean | (ref)                                                                    | 1.18x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 71.5 ms                                                                  | 59.1 ms: 1.21x faster                                                                  |
| float          | 59.5 ms                                                                  | 50.1 ms: 1.19x faster                                                                  |
| pidigits       | 145 ms                                                                   | 153 ms: 1.05x slower                                                                   |
| Geometric mean | (ref)                                                                    | 1.11x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                                   | 86.2 ms: 1.20x faster                                                                  |
| regex_v8       | 15.1 ms                                                                  | 13.7 ms: 1.10x faster                                                                  |
| regex_dna      | 131 ms                                                                   | 119 ms: 1.10x faster                                                                   |
| regex_effbot   | 1.64 ms                                                                  | 1.55 ms: 1.06x faster                                                                  |
| Geometric mean | (ref)                                                                    | 1.12x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|----------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps           | 9.00 ms                                                                  | 5.41 ms: 1.67x faster                                                                  |
| pickle_pure_python   | 264 us                                                                   | 186 us: 1.42x faster                                                                   |
| unpickle_pure_python | 179 us                                                                   | 127 us: 1.41x faster                                                                   |
| xml_etree_process    | 43.0 ms                                                                  | 36.9 ms: 1.17x faster                                                                  |
| unpickle             | 8.88 us                                                                  | 8.24 us: 1.08x faster                                                                  |
| json_loads           | 14.2 us                                                                  | 13.2 us: 1.08x faster                                                                  |
| xml_etree_parse      | 95.6 ms                                                                  | 91.0 ms: 1.05x faster                                                                  |
| pickle               | 6.67 us                                                                  | 6.84 us: 1.03x slower                                                                  |
| unpickle_list        | 2.71 us                                                                  | 2.90 us: 1.07x slower                                                                  |
| pickle_list          | 2.57 us                                                                  | 2.93 us: 1.14x slower                                                                  |
| pickle_dict          | 16.7 us                                                                  | 19.1 us: 1.15x slower                                                                  |
| Geometric mean       | (ref)                                                                    | 1.10x faster                                                                           |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 19.3 ms                                                                  | 19.0 ms: 1.02x faster                                                                  |
| python_startup_no_site | 14.8 ms                                                                  | 16.1 ms: 1.09x slower                                                                  |
| Geometric mean         | (ref)                                                                    | 1.03x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako            | 8.69 ms                                                                  | 6.37 ms: 1.37x faster                                                                  |
| django_template | 29.2 ms                                                                  | 22.3 ms: 1.31x faster                                                                  |
| genshi_text     | 18.5 ms                                                                  | 14.4 ms: 1.29x faster                                                                  |
| genshi_xml      | 38.8 ms                                                                  | 31.6 ms: 1.23x faster                                                                  |
| Geometric mean  | (ref)                                                                    | 1.30x faster                                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230407-pythonperf1-amd64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-2332a2e |
|-------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| deltablue               | 4.15 ms                                                                  | 2.00 ms: 2.07x faster                                                                  |
| logging_silent          | 94.6 ns                                                                  | 56.8 ns: 1.67x faster                                                                  |
| json_dumps              | 9.00 ms                                                                  | 5.41 ms: 1.67x faster                                                                  |
| go                      | 143 ms                                                                   | 88.5 ms: 1.62x faster                                                                  |
| scimark_lu              | 83.9 ms                                                                  | 52.9 ms: 1.59x faster                                                                  |
| richards                | 41.0 ms                                                                  | 26.1 ms: 1.57x faster                                                                  |
| sqlglot_parse           | 1.22 ms                                                                  | 782 us: 1.56x faster                                                                   |
| sqlglot_transpile       | 1.47 ms                                                                  | 976 us: 1.51x faster                                                                   |
| mypy2                   | 337 ms                                                                   | 225 ms: 1.50x faster                                                                   |
| raytrace                | 267 ms                                                                   | 179 ms: 1.50x faster                                                                   |
| generators              | 31.4 ms                                                                  | 21.3 ms: 1.48x faster                                                                  |
| pickle_pure_python      | 264 us                                                                   | 186 us: 1.42x faster                                                                   |
| unpack_sequence         | 39.4 ns                                                                  | 27.8 ns: 1.42x faster                                                                  |
| unpickle_pure_python    | 179 us                                                                   | 127 us: 1.41x faster                                                                   |
| chaos                   | 58.4 ms                                                                  | 42.3 ms: 1.38x faster                                                                  |
| hexiom                  | 5.45 ms                                                                  | 3.97 ms: 1.37x faster                                                                  |
| mako                    | 8.69 ms                                                                  | 6.37 ms: 1.37x faster                                                                  |
| asyncio_tcp             | 664 ms                                                                   | 488 ms: 1.36x faster                                                                   |
| crypto_pyaes            | 61.4 ms                                                                  | 45.4 ms: 1.35x faster                                                                  |
| pyflate                 | 388 ms                                                                   | 288 ms: 1.35x faster                                                                   |
| async_tree_io           | 1.02 sec                                                                 | 760 ms: 1.35x faster                                                                   |
| pycparser               | 873 ms                                                                   | 651 ms: 1.34x faster                                                                   |
| scimark_monte_carlo     | 56.0 ms                                                                  | 41.8 ms: 1.34x faster                                                                  |
| scimark_sor             | 104 ms                                                                   | 77.4 ms: 1.34x faster                                                                  |
| async_tree_none         | 414 ms                                                                   | 312 ms: 1.33x faster                                                                   |
| django_template         | 29.2 ms                                                                  | 22.3 ms: 1.31x faster                                                                  |
| genshi_text             | 18.5 ms                                                                  | 14.4 ms: 1.29x faster                                                                  |
| async_tree_memoization  | 485 ms                                                                   | 377 ms: 1.29x faster                                                                   |
| thrift                  | 632 us                                                                   | 494 us: 1.28x faster                                                                   |
| deepcopy_memo           | 28.4 us                                                                  | 22.6 us: 1.26x faster                                                                  |
| html5lib                | 47.3 ms                                                                  | 37.7 ms: 1.26x faster                                                                  |
| pprint_pformat          | 1.23 sec                                                                 | 984 ms: 1.25x faster                                                                   |
| chameleon               | 5.77 ms                                                                  | 4.66 ms: 1.24x faster                                                                  |
| genshi_xml              | 38.8 ms                                                                  | 31.6 ms: 1.23x faster                                                                  |
| async_tree_cpu_io_mixed | 604 ms                                                                   | 493 ms: 1.23x faster                                                                   |
| sqlglot_optimize        | 38.7 ms                                                                  | 31.6 ms: 1.22x faster                                                                  |
| pprint_safe_repr        | 593 ms                                                                   | 485 ms: 1.22x faster                                                                   |
| spectral_norm           | 74.3 ms                                                                  | 60.8 ms: 1.22x faster                                                                  |
| nbody                   | 71.5 ms                                                                  | 59.1 ms: 1.21x faster                                                                  |
| regex_compile           | 103 ms                                                                   | 86.2 ms: 1.20x faster                                                                  |
| float                   | 59.5 ms                                                                  | 50.1 ms: 1.19x faster                                                                  |
| json                    | 3.18 ms                                                                  | 2.71 ms: 1.17x faster                                                                  |
| tornado_http            | 106 ms                                                                   | 90.7 ms: 1.17x faster                                                                  |
| xml_etree_process       | 43.0 ms                                                                  | 36.9 ms: 1.17x faster                                                                  |
| sqlglot_normalize       | 201 ms                                                                   | 175 ms: 1.15x faster                                                                   |
| docutils                | 1.83 sec                                                                 | 1.60 sec: 1.15x faster                                                                 |
| scimark_fft             | 187 ms                                                                   | 164 ms: 1.14x faster                                                                   |
| deepcopy                | 256 us                                                                   | 229 us: 1.12x faster                                                                   |
| bench_thread_pool       | 953 us                                                                   | 855 us: 1.11x faster                                                                   |
| scimark_sparse_mat_mult | 2.67 ms                                                                  | 2.40 ms: 1.11x faster                                                                  |
| mdp                     | 1.60 sec                                                                 | 1.45 sec: 1.11x faster                                                                 |
| sympy_expand            | 313 ms                                                                   | 283 ms: 1.11x faster                                                                   |
| regex_v8                | 15.1 ms                                                                  | 13.7 ms: 1.10x faster                                                                  |
| regex_dna               | 131 ms                                                                   | 119 ms: 1.10x faster                                                                   |
| create_gc_cycles        | 764 us                                                                   | 695 us: 1.10x faster                                                                   |
| sympy_integrate         | 14.7 ms                                                                  | 13.4 ms: 1.10x faster                                                                  |
| nqueens                 | 64.8 ms                                                                  | 59.1 ms: 1.10x faster                                                                  |
| dulwich_log             | 47.0 ms                                                                  | 42.9 ms: 1.10x faster                                                                  |
| deepcopy_reduce         | 2.18 us                                                                  | 2.00 us: 1.09x faster                                                                  |
| 2to3                    | 229 ms                                                                   | 210 ms: 1.09x faster                                                                   |
| unpickle                | 8.88 us                                                                  | 8.24 us: 1.08x faster                                                                  |
| json_loads              | 14.2 us                                                                  | 13.2 us: 1.08x faster                                                                  |
| sqlite_synth            | 1.85 us                                                                  | 1.72 us: 1.07x faster                                                                  |
| coroutines              | 15.6 ms                                                                  | 14.7 ms: 1.07x faster                                                                  |
| comprehensions          | 16.0 us                                                                  | 15.0 us: 1.07x faster                                                                  |
| regex_effbot            | 1.64 ms                                                                  | 1.55 ms: 1.06x faster                                                                  |
| sympy_str               | 189 ms                                                                   | 179 ms: 1.05x faster                                                                   |
| xml_etree_parse         | 95.6 ms                                                                  | 91.0 ms: 1.05x faster                                                                  |
| sympy_sum               | 102 ms                                                                   | 100 ms: 1.02x faster                                                                   |
| python_startup          | 19.3 ms                                                                  | 19.0 ms: 1.02x faster                                                                  |
| meteor_contest          | 74.3 ms                                                                  | 73.3 ms: 1.01x faster                                                                  |
| pickle                  | 6.67 us                                                                  | 6.84 us: 1.03x slower                                                                  |
| telco                   | 3.77 ms                                                                  | 3.90 ms: 1.04x slower                                                                  |
| logging_format          | 6.53 us                                                                  | 6.84 us: 1.05x slower                                                                  |
| logging_simple          | 6.12 us                                                                  | 6.43 us: 1.05x slower                                                                  |
| pidigits                | 145 ms                                                                   | 153 ms: 1.05x slower                                                                   |
| unpickle_list           | 2.71 us                                                                  | 2.90 us: 1.07x slower                                                                  |
| python_startup_no_site  | 14.8 ms                                                                  | 16.1 ms: 1.09x slower                                                                  |
| gc_traversal            | 1.33 ms                                                                  | 1.48 ms: 1.12x slower                                                                  |
| bench_mp_pool           | 59.2 ms                                                                  | 66.9 ms: 1.13x slower                                                                  |
| pickle_list             | 2.57 us                                                                  | 2.93 us: 1.14x slower                                                                  |
| pathlib                 | 75.2 ms                                                                  | 86.1 ms: 1.15x slower                                                                  |
| pickle_dict             | 16.7 us                                                                  | 19.1 us: 1.15x slower                                                                  |
| dask                    | 310 ms                                                                   | 357 ms: 1.15x slower                                                                   |
| coverage                | 37.5 ms                                                                  | 52.1 ms: 1.39x slower                                                                  |
| Geometric mean          | (ref)                                                                    | 1.17x faster                                                                           |

Benchmark hidden because not significant (4): fannkuch, async_generators, xml_etree_generate, xml_etree_iterparse
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
