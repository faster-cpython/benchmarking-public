
# Results vs. 3.11.0

- fork: faster-cpython
- ref: micro_op_jump_if_non
- machine: windows-amd64
- commit hash: 66a6bc3
- commit date: 2023-07-10
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-pythonperf1-amd64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| docutils       | 1.60 sec                                                    | 1.67 sec: 1.04x slower                                                               |
| tornado_http   | 91.8 ms                                                     | 101 ms: 1.10x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-pythonperf1-amd64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                                 |
| float          | 54.6 ms                                                     | 56.0 ms: 1.02x slower                                                                |
| nbody          | 70.0 ms                                                     | 77.8 ms: 1.11x slower                                                                |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-pythonperf1-amd64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 13.8 ms                                                     | 13.7 ms: 1.01x faster                                                                |
| regex_compile  | 90.6 ms                                                     | 93.1 ms: 1.03x slower                                                                |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                                 |
| regex_effbot   | 1.50 ms                                                     | 1.59 ms: 1.06x slower                                                                |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-pythonperf1-amd64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.68 ms: 1.33x faster                                                                |
| unpickle_pure_python | 152 us                                                      | 143 us: 1.06x faster                                                                 |
| xml_etree_parse      | 95.9 ms                                                     | 93.9 ms: 1.02x faster                                                                |
| pickle_dict          | 18.5 us                                                     | 18.2 us: 1.02x faster                                                                |
| pickle_pure_python   | 200 us                                                      | 198 us: 1.01x faster                                                                 |
| unpickle             | 8.09 us                                                     | 8.39 us: 1.04x slower                                                                |
| xml_etree_iterparse  | 62.6 ms                                                     | 65.4 ms: 1.05x slower                                                                |
| json_loads           | 12.9 us                                                     | 13.5 us: 1.05x slower                                                                |
| pickle               | 6.61 us                                                     | 6.96 us: 1.05x slower                                                                |
| pickle_list          | 2.68 us                                                     | 2.84 us: 1.06x slower                                                                |
| xml_etree_process    | 37.1 ms                                                     | 39.5 ms: 1.07x slower                                                                |
| unpickle_list        | 2.55 us                                                     | 2.81 us: 1.10x slower                                                                |
| xml_etree_generate   | 52.2 ms                                                     | 57.7 ms: 1.10x slower                                                                |
| tomli_loads          | 1.41 sec                                                    | 1.65 sec: 1.16x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-pythonperf1-amd64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 16.9 ms: 1.06x slower                                                                |
| python_startup         | 18.7 ms                                                     | 20.0 ms: 1.07x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-pythonperf1-amd64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|-----------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 7.53 ms: 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230710-pythonperf1-amd64-faster%2dcpython-micro_op_jump_if_non-3.13.0a0-66a6bc3 |
|--------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 93.6 us: 3.44x faster                                                                |
| generators               | 33.8 ms                                                     | 25.1 ms: 1.35x faster                                                                |
| json_dumps               | 7.56 ms                                                     | 5.68 ms: 1.33x faster                                                                |
| asyncio_tcp              | 699 ms                                                      | 547 ms: 1.28x faster                                                                 |
| raytrace                 | 211 ms                                                      | 183 ms: 1.15x faster                                                                 |
| mdp                      | 1.67 sec                                                    | 1.46 sec: 1.14x faster                                                               |
| unpack_sequence          | 46.1 ns                                                     | 40.3 ns: 1.14x faster                                                                |
| json                     | 3.25 ms                                                     | 2.87 ms: 1.14x faster                                                                |
| deltablue                | 2.61 ms                                                     | 2.32 ms: 1.13x faster                                                                |
| richards_super           | 37.5 ms                                                     | 33.9 ms: 1.10x faster                                                                |
| sqlglot_parse            | 952 us                                                      | 864 us: 1.10x faster                                                                 |
| chaos                    | 47.1 ms                                                     | 43.0 ms: 1.10x faster                                                                |
| coverage                 | 55.9 ms                                                     | 51.2 ms: 1.09x faster                                                                |
| logging_silent           | 69.8 ns                                                     | 64.8 ns: 1.08x faster                                                                |
| async_tree_none          | 320 ms                                                      | 299 ms: 1.07x faster                                                                 |
| sqlglot_transpile        | 1.16 ms                                                     | 1.09 ms: 1.07x faster                                                                |
| unpickle_pure_python     | 152 us                                                      | 143 us: 1.06x faster                                                                 |
| async_tree_memoization   | 371 ms                                                      | 350 ms: 1.06x faster                                                                 |
| async_tree_io            | 779 ms                                                      | 746 ms: 1.04x faster                                                                 |
| comprehensions           | 15.9 us                                                     | 15.3 us: 1.04x faster                                                                |
| scimark_lu               | 63.5 ms                                                     | 61.1 ms: 1.04x faster                                                                |
| crypto_pyaes             | 47.6 ms                                                     | 45.9 ms: 1.04x faster                                                                |
| mypy2                    | 229 ms                                                      | 222 ms: 1.03x faster                                                                 |
| spectral_norm            | 67.9 ms                                                     | 65.9 ms: 1.03x faster                                                                |
| hexiom                   | 4.55 ms                                                     | 4.42 ms: 1.03x faster                                                                |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 488 ms: 1.03x faster                                                                 |
| xml_etree_parse          | 95.9 ms                                                     | 93.9 ms: 1.02x faster                                                                |
| scimark_monte_carlo      | 44.6 ms                                                     | 43.8 ms: 1.02x faster                                                                |
| pickle_dict              | 18.5 us                                                     | 18.2 us: 1.02x faster                                                                |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.53 ms: 1.02x faster                                                                |
| richards                 | 30.6 ms                                                     | 30.1 ms: 1.01x faster                                                                |
| pickle_pure_python       | 200 us                                                      | 198 us: 1.01x faster                                                                 |
| regex_v8                 | 13.8 ms                                                     | 13.7 ms: 1.01x faster                                                                |
| go                       | 97.3 ms                                                     | 96.6 ms: 1.01x faster                                                                |
| dulwich_log              | 44.5 ms                                                     | 44.9 ms: 1.01x slower                                                                |
| pidigits                 | 148 ms                                                      | 150 ms: 1.01x slower                                                                 |
| sqlglot_normalize        | 190 ms                                                      | 193 ms: 1.02x slower                                                                 |
| bench_thread_pool        | 852 us                                                      | 872 us: 1.02x slower                                                                 |
| float                    | 54.6 ms                                                     | 56.0 ms: 1.02x slower                                                                |
| gc_traversal             | 1.46 ms                                                     | 1.50 ms: 1.03x slower                                                                |
| sqlglot_optimize         | 34.9 ms                                                     | 35.8 ms: 1.03x slower                                                                |
| pyflate                  | 304 ms                                                      | 312 ms: 1.03x slower                                                                 |
| regex_compile            | 90.6 ms                                                     | 93.1 ms: 1.03x slower                                                                |
| logging_simple           | 6.61 us                                                     | 6.84 us: 1.03x slower                                                                |
| coroutines               | 14.6 ms                                                     | 15.1 ms: 1.04x slower                                                                |
| mako                     | 7.26 ms                                                     | 7.53 ms: 1.04x slower                                                                |
| unpickle                 | 8.09 us                                                     | 8.39 us: 1.04x slower                                                                |
| regex_dna                | 115 ms                                                      | 120 ms: 1.04x slower                                                                 |
| docutils                 | 1.60 sec                                                    | 1.67 sec: 1.04x slower                                                               |
| xml_etree_iterparse      | 62.6 ms                                                     | 65.4 ms: 1.05x slower                                                                |
| json_loads               | 12.9 us                                                     | 13.5 us: 1.05x slower                                                                |
| logging_format           | 7.01 us                                                     | 7.35 us: 1.05x slower                                                                |
| scimark_fft              | 178 ms                                                      | 187 ms: 1.05x slower                                                                 |
| pickle                   | 6.61 us                                                     | 6.96 us: 1.05x slower                                                                |
| sqlite_synth             | 1.68 us                                                     | 1.77 us: 1.05x slower                                                                |
| create_gc_cycles         | 693 us                                                      | 733 us: 1.06x slower                                                                 |
| regex_effbot             | 1.50 ms                                                     | 1.59 ms: 1.06x slower                                                                |
| pickle_list              | 2.68 us                                                     | 2.84 us: 1.06x slower                                                                |
| pprint_safe_repr         | 512 ms                                                      | 543 ms: 1.06x slower                                                                 |
| python_startup_no_site   | 15.9 ms                                                     | 16.9 ms: 1.06x slower                                                                |
| xml_etree_process        | 37.1 ms                                                     | 39.5 ms: 1.07x slower                                                                |
| python_startup           | 18.7 ms                                                     | 20.0 ms: 1.07x slower                                                                |
| pprint_pformat           | 1.04 sec                                                    | 1.11 sec: 1.07x slower                                                               |
| bench_mp_pool            | 62.5 ms                                                     | 67.1 ms: 1.07x slower                                                                |
| deepcopy_reduce          | 2.07 us                                                     | 2.24 us: 1.08x slower                                                                |
| scimark_sor              | 75.6 ms                                                     | 82.3 ms: 1.09x slower                                                                |
| tornado_http             | 91.8 ms                                                     | 101 ms: 1.10x slower                                                                 |
| unpickle_list            | 2.55 us                                                     | 2.81 us: 1.10x slower                                                                |
| xml_etree_generate       | 52.2 ms                                                     | 57.7 ms: 1.10x slower                                                                |
| nbody                    | 70.0 ms                                                     | 77.8 ms: 1.11x slower                                                                |
| pycparser                | 691 ms                                                      | 780 ms: 1.13x slower                                                                 |
| pathlib                  | 71.4 ms                                                     | 82.9 ms: 1.16x slower                                                                |
| tomli_loads              | 1.41 sec                                                    | 1.65 sec: 1.16x slower                                                               |
| telco                    | 3.90 ms                                                     | 5.05 ms: 1.29x slower                                                                |
| async_generators         | 178 ms                                                      | 240 ms: 1.35x slower                                                                 |
| dask                     | 264 ms                                                      | 383 ms: 1.45x slower                                                                 |
| Geometric mean           | (ref)                                                       | 1.01x faster                                                                         |

Benchmark hidden because not significant (6): asyncio_tcp_ssl, nqueens, meteor_contest, deepcopy_memo, deepcopy, fannkuch
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
