
# Results vs. 3.10.4

- fork: python
- ref: 3d5d3f7af6498effbc60
- machine: linux-x86_64
- commit hash: 3d5d3f7
- commit date: 2023-01-10
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 253 ms: 1.33x faster                                                  |
| chameleon      | 9.13 ms                                                             | 6.46 ms: 1.41x faster                                                 |
| docutils       | 3.19 sec                                                            | 2.48 sec: 1.29x faster                                                |
| html5lib       | 86.4 ms                                                             | 59.8 ms: 1.44x faster                                                 |
| Geometric mean | (ref)                                                               | 1.37x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 93.1 ms: 1.57x faster                                                 |
| float          | 110 ms                                                              | 72.2 ms: 1.52x faster                                                 |
| pidigits       | 190 ms                                                              | 192 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                               | 1.33x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 132 ms: 1.34x faster                                                  |
| regex_v8       | 24.9 ms                                                             | 21.1 ms: 1.18x faster                                                 |
| regex_dna      | 213 ms                                                              | 209 ms: 1.02x faster                                                  |
| regex_effbot   | 3.22 ms                                                             | 3.49 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                               | 1.11x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 285 us: 1.60x faster                                                  |
| unpickle_pure_python | 300 us                                                              | 200 us: 1.50x faster                                                  |
| json_dumps           | 13.7 ms                                                             | 9.54 ms: 1.44x faster                                                 |
| xml_etree_process    | 74.8 ms                                                             | 53.9 ms: 1.39x faster                                                 |
| xml_etree_generate   | 94.9 ms                                                             | 77.5 ms: 1.22x faster                                                 |
| json_loads           | 29.3 us                                                             | 24.3 us: 1.20x faster                                                 |
| pickle_list          | 4.73 us                                                             | 4.02 us: 1.18x faster                                                 |
| unpickle             | 15.0 us                                                             | 13.0 us: 1.16x faster                                                 |
| xml_etree_parse      | 164 ms                                                              | 149 ms: 1.10x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                              | 106 ms: 1.05x faster                                                  |
| pickle               | 10.2 us                                                             | 10.0 us: 1.02x faster                                                 |
| pickle_dict          | 27.8 us                                                             | 30.0 us: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                               | 1.20x faster                                                          |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.54 ms: 1.66x faster                                                 |
| python_startup_no_site | 5.80 ms                                                             | 6.09 ms: 1.05x slower                                                 |
| Geometric mean         | (ref)                                                               | 1.26x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 9.74 ms: 1.51x faster                                                 |
| genshi_text     | 30.4 ms                                                             | 20.8 ms: 1.46x faster                                                 |
| django_template | 45.8 ms                                                             | 32.6 ms: 1.41x faster                                                 |
| genshi_xml      | 64.3 ms                                                             | 46.5 ms: 1.38x faster                                                 |
| Geometric mean  | (ref)                                                               | 1.44x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230110-linux-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| deltablue               | 7.30 ms                                                             | 3.25 ms: 2.24x faster                                                 |
| asyncio_tcp             | 922 ms                                                              | 504 ms: 1.83x faster                                                  |
| scimark_sor             | 198 ms                                                              | 108 ms: 1.82x faster                                                  |
| logging_silent          | 169 ns                                                              | 93.5 ns: 1.81x faster                                                 |
| richards                | 74.2 ms                                                             | 42.3 ms: 1.75x faster                                                 |
| pyflate                 | 671 ms                                                              | 397 ms: 1.69x faster                                                  |
| go                      | 226 ms                                                              | 135 ms: 1.67x faster                                                  |
| raytrace                | 470 ms                                                              | 284 ms: 1.66x faster                                                  |
| python_startup          | 14.1 ms                                                             | 8.54 ms: 1.66x faster                                                 |
| scimark_monte_carlo     | 109 ms                                                              | 65.7 ms: 1.65x faster                                                 |
| pickle_pure_python      | 457 us                                                              | 285 us: 1.60x faster                                                  |
| hexiom                  | 9.50 ms                                                             | 5.98 ms: 1.59x faster                                                 |
| unpack_sequence         | 65.6 ns                                                             | 41.4 ns: 1.59x faster                                                 |
| spectral_norm           | 150 ms                                                              | 95.0 ms: 1.58x faster                                                 |
| nbody                   | 146 ms                                                              | 93.1 ms: 1.57x faster                                                 |
| chaos                   | 106 ms                                                              | 67.7 ms: 1.56x faster                                                 |
| crypto_pyaes            | 117 ms                                                              | 75.7 ms: 1.54x faster                                                 |
| float                   | 110 ms                                                              | 72.2 ms: 1.52x faster                                                 |
| mako                    | 14.7 ms                                                             | 9.74 ms: 1.51x faster                                                 |
| unpickle_pure_python    | 300 us                                                              | 200 us: 1.50x faster                                                  |
| deepcopy_memo           | 51.8 us                                                             | 34.7 us: 1.49x faster                                                 |
| scimark_lu              | 160 ms                                                              | 107 ms: 1.49x faster                                                  |
| sqlglot_parse           | 2.07 ms                                                             | 1.41 ms: 1.47x faster                                                 |
| genshi_text             | 30.4 ms                                                             | 20.8 ms: 1.46x faster                                                 |
| sqlglot_transpile       | 2.45 ms                                                             | 1.69 ms: 1.45x faster                                                 |
| html5lib                | 86.4 ms                                                             | 59.8 ms: 1.44x faster                                                 |
| json_dumps              | 13.7 ms                                                             | 9.54 ms: 1.44x faster                                                 |
| pprint_pformat          | 1.98 sec                                                            | 1.38 sec: 1.43x faster                                                |
| logging_format          | 9.07 us                                                             | 6.35 us: 1.43x faster                                                 |
| logging_simple          | 8.21 us                                                             | 5.77 us: 1.42x faster                                                 |
| pycparser               | 1.53 sec                                                            | 1.08 sec: 1.42x faster                                                |
| chameleon               | 9.13 ms                                                             | 6.46 ms: 1.41x faster                                                 |
| django_template         | 45.8 ms                                                             | 32.6 ms: 1.41x faster                                                 |
| pprint_safe_repr        | 953 ms                                                              | 680 ms: 1.40x faster                                                  |
| xml_etree_process       | 74.8 ms                                                             | 53.9 ms: 1.39x faster                                                 |
| async_tree_memoization  | 853 ms                                                              | 616 ms: 1.38x faster                                                  |
| genshi_xml              | 64.3 ms                                                             | 46.5 ms: 1.38x faster                                                 |
| thrift                  | 1.04 ms                                                             | 752 us: 1.38x faster                                                  |
| async_tree_io           | 1.78 sec                                                            | 1.30 sec: 1.37x faster                                                |
| async_tree_none         | 713 ms                                                              | 521 ms: 1.37x faster                                                  |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.13 ms: 1.36x faster                                                 |
| scimark_fft             | 425 ms                                                              | 314 ms: 1.35x faster                                                  |
| regex_compile           | 177 ms                                                              | 132 ms: 1.34x faster                                                  |
| fannkuch                | 485 ms                                                              | 362 ms: 1.34x faster                                                  |
| 2to3                    | 336 ms                                                              | 253 ms: 1.33x faster                                                  |
| mypy2                   | 432 ms                                                              | 332 ms: 1.30x faster                                                  |
| sqlglot_normalize       | 135 ms                                                              | 104 ms: 1.29x faster                                                  |
| deepcopy                | 438 us                                                              | 339 us: 1.29x faster                                                  |
| sqlglot_optimize        | 65.3 ms                                                             | 50.7 ms: 1.29x faster                                                 |
| docutils                | 3.19 sec                                                            | 2.48 sec: 1.29x faster                                                |
| deepcopy_reduce         | 3.80 us                                                             | 2.99 us: 1.27x faster                                                 |
| nqueens                 | 98.8 ms                                                             | 78.0 ms: 1.27x faster                                                 |
| async_tree_cpu_io_mixed | 944 ms                                                              | 747 ms: 1.26x faster                                                  |
| coroutines              | 31.8 ms                                                             | 25.4 ms: 1.25x faster                                                 |
| dask                    | 437 ms                                                              | 355 ms: 1.23x faster                                                  |
| dulwich_log             | 76.3 ms                                                             | 62.1 ms: 1.23x faster                                                 |
| xml_etree_generate      | 94.9 ms                                                             | 77.5 ms: 1.22x faster                                                 |
| bench_thread_pool       | 954 us                                                              | 782 us: 1.22x faster                                                  |
| json_loads              | 29.3 us                                                             | 24.3 us: 1.20x faster                                                 |
| sympy_integrate         | 24.3 ms                                                             | 20.3 ms: 1.20x faster                                                 |
| sympy_expand            | 540 ms                                                              | 455 ms: 1.19x faster                                                  |
| async_generators        | 420 ms                                                              | 354 ms: 1.19x faster                                                  |
| regex_v8                | 24.9 ms                                                             | 21.1 ms: 1.18x faster                                                 |
| pickle_list             | 4.73 us                                                             | 4.02 us: 1.18x faster                                                 |
| djangocms               | 36.3 us                                                             | 30.9 us: 1.17x faster                                                 |
| sympy_str               | 328 ms                                                              | 282 ms: 1.16x faster                                                  |
| sqlite_synth            | 2.97 us                                                             | 2.57 us: 1.16x faster                                                 |
| unpickle                | 15.0 us                                                             | 13.0 us: 1.16x faster                                                 |
| comprehensions          | 27.3 us                                                             | 23.7 us: 1.15x faster                                                 |
| json                    | 5.41 ms                                                             | 4.74 ms: 1.14x faster                                                 |
| sympy_sum               | 185 ms                                                              | 163 ms: 1.14x faster                                                  |
| create_gc_cycles        | 1.64 ms                                                             | 1.45 ms: 1.13x faster                                                 |
| meteor_contest          | 115 ms                                                              | 104 ms: 1.10x faster                                                  |
| xml_etree_parse         | 164 ms                                                              | 149 ms: 1.10x faster                                                  |
| pathlib                 | 19.8 ms                                                             | 18.0 ms: 1.10x faster                                                 |
| telco                   | 6.67 ms                                                             | 6.26 ms: 1.07x faster                                                 |
| xml_etree_iterparse     | 111 ms                                                              | 106 ms: 1.05x faster                                                  |
| mdp                     | 2.75 sec                                                            | 2.66 sec: 1.04x faster                                                |
| pickle                  | 10.2 us                                                             | 10.0 us: 1.02x faster                                                 |
| regex_dna               | 213 ms                                                              | 209 ms: 1.02x faster                                                  |
| gc_traversal            | 3.53 ms                                                             | 3.57 ms: 1.01x slower                                                 |
| pidigits                | 190 ms                                                              | 192 ms: 1.01x slower                                                  |
| generators              | 75.7 ms                                                             | 79.1 ms: 1.05x slower                                                 |
| python_startup_no_site  | 5.80 ms                                                             | 6.09 ms: 1.05x slower                                                 |
| pickle_dict             | 27.8 us                                                             | 30.0 us: 1.08x slower                                                 |
| regex_effbot            | 3.22 ms                                                             | 3.49 ms: 1.08x slower                                                 |
| coverage                | 70.6 ms                                                             | 99.0 ms: 1.40x slower                                                 |
| Geometric mean          | (ref)                                                               | 1.30x faster                                                          |

Benchmark hidden because not significant (2): bench_mp_pool, unpickle_list
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
