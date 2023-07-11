
# Results vs. 3.10.4

- fork: faster-cpython
- ref: micro_op_jump_if_non
- machine: windows-amd64
- commit hash: 66a6bc3
- commit date: 2023-07-10
- overall geometric mean: 1.13x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-pythonperf1-amd64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| docutils       | 1.89 sec                                                    | 1.67 sec: 1.13x faster                                                               |
| tornado_http   | 109 ms                                                      | 101 ms: 1.08x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-pythonperf1-amd64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 56.0 ms: 1.08x faster                                                                |
| pidigits       | 145 ms                                                      | 150 ms: 1.03x slower                                                                 |
| nbody          | 69.3 ms                                                     | 77.8 ms: 1.12x slower                                                                |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-pythonperf1-amd64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 93.1 ms: 1.11x faster                                                                |
| regex_dna      | 132 ms                                                      | 120 ms: 1.10x faster                                                                 |
| regex_v8       | 15.0 ms                                                     | 13.7 ms: 1.10x faster                                                                |
| regex_effbot   | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                                                |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-pythonperf1-amd64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.68 ms: 1.50x faster                                                                |
| pickle_pure_python   | 257 us                                                      | 198 us: 1.30x faster                                                                 |
| unpickle_pure_python | 171 us                                                      | 143 us: 1.20x faster                                                                 |
| xml_etree_process    | 43.4 ms                                                     | 39.5 ms: 1.10x faster                                                                |
| unpickle             | 9.17 us                                                     | 8.39 us: 1.09x faster                                                                |
| xml_etree_parse      | 102 ms                                                      | 93.9 ms: 1.08x faster                                                                |
| json_loads           | 14.2 us                                                     | 13.5 us: 1.05x faster                                                                |
| tomli_loads          | 1.62 sec                                                    | 1.65 sec: 1.02x slower                                                               |
| pickle               | 6.80 us                                                     | 6.96 us: 1.02x slower                                                                |
| xml_etree_iterparse  | 63.5 ms                                                     | 65.4 ms: 1.03x slower                                                                |
| xml_etree_generate   | 54.5 ms                                                     | 57.7 ms: 1.06x slower                                                                |
| pickle_dict          | 16.9 us                                                     | 18.2 us: 1.07x slower                                                                |
| pickle_list          | 2.59 us                                                     | 2.84 us: 1.10x slower                                                                |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                                         |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-pythonperf1-amd64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 16.9 ms: 1.09x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.04x slower                                                                         |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-pythonperf1-amd64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|-----------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 7.53 ms: 1.17x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230710-pythonperf1-amd64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 325 us                                                      | 93.6 us: 3.47x faster                                                                |
| deltablue                | 4.17 ms                                                     | 2.32 ms: 1.80x faster                                                                |
| mypy2                    | 352 ms                                                      | 222 ms: 1.59x faster                                                                 |
| richards_super           | 51.7 ms                                                     | 33.9 ms: 1.52x faster                                                                |
| json_dumps               | 8.50 ms                                                     | 5.68 ms: 1.50x faster                                                                |
| logging_silent           | 96.4 ns                                                     | 64.8 ns: 1.49x faster                                                                |
| raytrace                 | 271 ms                                                      | 183 ms: 1.48x faster                                                                 |
| async_tree_io            | 1.07 sec                                                    | 746 ms: 1.43x faster                                                                 |
| async_tree_memoization   | 497 ms                                                      | 350 ms: 1.42x faster                                                                 |
| sqlglot_parse            | 1.22 ms                                                     | 864 us: 1.41x faster                                                                 |
| go                       | 136 ms                                                      | 96.6 ms: 1.41x faster                                                                |
| async_tree_none          | 420 ms                                                      | 299 ms: 1.40x faster                                                                 |
| scimark_lu               | 85.4 ms                                                     | 61.1 ms: 1.40x faster                                                                |
| chaos                    | 58.9 ms                                                     | 43.0 ms: 1.37x faster                                                                |
| richards                 | 41.2 ms                                                     | 30.1 ms: 1.37x faster                                                                |
| crypto_pyaes             | 62.3 ms                                                     | 45.9 ms: 1.36x faster                                                                |
| sqlglot_transpile        | 1.46 ms                                                     | 1.09 ms: 1.34x faster                                                                |
| asyncio_tcp              | 712 ms                                                      | 547 ms: 1.30x faster                                                                 |
| pickle_pure_python       | 257 us                                                      | 198 us: 1.30x faster                                                                 |
| scimark_monte_carlo      | 55.9 ms                                                     | 43.8 ms: 1.28x faster                                                                |
| scimark_sor              | 105 ms                                                      | 82.3 ms: 1.27x faster                                                                |
| generators               | 31.6 ms                                                     | 25.1 ms: 1.26x faster                                                                |
| hexiom                   | 5.52 ms                                                     | 4.42 ms: 1.25x faster                                                                |
| async_tree_cpu_io_mixed  | 609 ms                                                      | 488 ms: 1.25x faster                                                                 |
| pyflate                  | 387 ms                                                      | 312 ms: 1.24x faster                                                                 |
| unpickle_pure_python     | 171 us                                                      | 143 us: 1.20x faster                                                                 |
| spectral_norm            | 78.0 ms                                                     | 65.9 ms: 1.18x faster                                                                |
| mdp                      | 1.71 sec                                                    | 1.46 sec: 1.17x faster                                                               |
| mako                     | 8.80 ms                                                     | 7.53 ms: 1.17x faster                                                                |
| docutils                 | 1.89 sec                                                    | 1.67 sec: 1.13x faster                                                               |
| deepcopy_memo            | 28.5 us                                                     | 25.2 us: 1.13x faster                                                                |
| pycparser                | 868 ms                                                      | 780 ms: 1.11x faster                                                                 |
| regex_compile            | 103 ms                                                      | 93.1 ms: 1.11x faster                                                                |
| regex_dna                | 132 ms                                                      | 120 ms: 1.10x faster                                                                 |
| xml_etree_process        | 43.4 ms                                                     | 39.5 ms: 1.10x faster                                                                |
| regex_v8                 | 15.0 ms                                                     | 13.7 ms: 1.10x faster                                                                |
| unpickle                 | 9.17 us                                                     | 8.39 us: 1.09x faster                                                                |
| sqlglot_optimize         | 39.0 ms                                                     | 35.8 ms: 1.09x faster                                                                |
| bench_thread_pool        | 946 us                                                      | 872 us: 1.09x faster                                                                 |
| pprint_pformat           | 1.21 sec                                                    | 1.11 sec: 1.09x faster                                                               |
| pprint_safe_repr         | 589 ms                                                      | 543 ms: 1.08x faster                                                                 |
| xml_etree_parse          | 102 ms                                                      | 93.9 ms: 1.08x faster                                                                |
| tornado_http             | 109 ms                                                      | 101 ms: 1.08x faster                                                                 |
| float                    | 60.2 ms                                                     | 56.0 ms: 1.08x faster                                                                |
| create_gc_cycles         | 782 us                                                      | 733 us: 1.07x faster                                                                 |
| json                     | 3.05 ms                                                     | 2.87 ms: 1.06x faster                                                                |
| dulwich_log              | 47.6 ms                                                     | 44.9 ms: 1.06x faster                                                                |
| coroutines               | 15.9 ms                                                     | 15.1 ms: 1.05x faster                                                                |
| scimark_sparse_mat_mult  | 2.66 ms                                                     | 2.53 ms: 1.05x faster                                                                |
| regex_effbot             | 1.66 ms                                                     | 1.59 ms: 1.05x faster                                                                |
| json_loads               | 14.2 us                                                     | 13.5 us: 1.05x faster                                                                |
| sqlglot_normalize        | 202 ms                                                      | 193 ms: 1.05x faster                                                                 |
| comprehensions           | 16.0 us                                                     | 15.3 us: 1.05x faster                                                                |
| sqlite_synth             | 1.84 us                                                     | 1.77 us: 1.04x faster                                                                |
| nqueens                  | 67.0 ms                                                     | 64.7 ms: 1.04x faster                                                                |
| deepcopy                 | 255 us                                                      | 247 us: 1.03x faster                                                                 |
| scimark_fft              | 193 ms                                                      | 187 ms: 1.03x faster                                                                 |
| fannkuch                 | 258 ms                                                      | 253 ms: 1.02x faster                                                                 |
| tomli_loads              | 1.62 sec                                                    | 1.65 sec: 1.02x slower                                                               |
| pickle                   | 6.80 us                                                     | 6.96 us: 1.02x slower                                                                |
| meteor_contest           | 72.5 ms                                                     | 74.7 ms: 1.03x slower                                                                |
| xml_etree_iterparse      | 63.5 ms                                                     | 65.4 ms: 1.03x slower                                                                |
| pidigits                 | 145 ms                                                      | 150 ms: 1.03x slower                                                                 |
| deepcopy_reduce          | 2.16 us                                                     | 2.24 us: 1.04x slower                                                                |
| xml_etree_generate       | 54.5 ms                                                     | 57.7 ms: 1.06x slower                                                                |
| unpack_sequence          | 37.8 ns                                                     | 40.3 ns: 1.07x slower                                                                |
| async_generators         | 224 ms                                                      | 240 ms: 1.07x slower                                                                 |
| pathlib                  | 77.4 ms                                                     | 82.9 ms: 1.07x slower                                                                |
| pickle_dict              | 16.9 us                                                     | 18.2 us: 1.07x slower                                                                |
| python_startup_no_site   | 15.5 ms                                                     | 16.9 ms: 1.09x slower                                                                |
| pickle_list              | 2.59 us                                                     | 2.84 us: 1.10x slower                                                                |
| logging_simple           | 6.20 us                                                     | 6.84 us: 1.10x slower                                                                |
| logging_format           | 6.66 us                                                     | 7.35 us: 1.10x slower                                                                |
| bench_mp_pool            | 60.7 ms                                                     | 67.1 ms: 1.11x slower                                                                |
| gc_traversal             | 1.34 ms                                                     | 1.50 ms: 1.11x slower                                                                |
| nbody                    | 69.3 ms                                                     | 77.8 ms: 1.12x slower                                                                |
| dask                     | 305 ms                                                      | 383 ms: 1.26x slower                                                                 |
| coverage                 | 40.0 ms                                                     | 51.2 ms: 1.28x slower                                                                |
| telco                    | 3.78 ms                                                     | 5.05 ms: 1.34x slower                                                                |
| Geometric mean           | (ref)                                                       | 1.13x faster                                                                         |

Benchmark hidden because not significant (3): unpickle_list, python_startup, asyncio_tcp_ssl
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
