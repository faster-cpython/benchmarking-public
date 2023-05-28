
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 3a5be87
- commit date: 2023-05-28
- overall geometric mean: 1.07x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-pythonperf1-amd64-python-main-3.13.0a0-3a5be87 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| html5lib       | 37.5 ms                                                     | 35.8 ms: 1.05x faster                                      |
| tornado_http   | 91.8 ms                                                     | 89.4 ms: 1.03x faster                                      |
| Geometric mean | (ref)                                                       | 1.02x faster                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-pythonperf1-amd64-python-main-3.13.0a0-3a5be87 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 54.6 ms                                                     | 52.2 ms: 1.05x faster                                      |
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                               |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-pythonperf1-amd64-python-main-3.13.0a0-3a5be87 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 85.4 ms: 1.06x faster                                      |
| regex_v8       | 13.8 ms                                                     | 14.3 ms: 1.03x slower                                      |
| regex_dna      | 115 ms                                                      | 124 ms: 1.07x slower                                       |
| regex_effbot   | 1.50 ms                                                     | 1.66 ms: 1.11x slower                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-pythonperf1-amd64-python-main-3.13.0a0-3a5be87 |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.64 ms: 1.34x faster                                      |
| unpickle_pure_python | 152 us                                                      | 132 us: 1.15x faster                                       |
| tomli_loads          | 1.41 sec                                                    | 1.34 sec: 1.06x faster                                     |
| pickle_pure_python   | 200 us                                                      | 190 us: 1.05x faster                                       |
| xml_etree_parse      | 95.9 ms                                                     | 91.7 ms: 1.05x faster                                      |
| xml_etree_iterparse  | 62.6 ms                                                     | 63.3 ms: 1.01x slower                                      |
| json_loads           | 12.9 us                                                     | 13.4 us: 1.04x slower                                      |
| xml_etree_generate   | 52.2 ms                                                     | 54.8 ms: 1.05x slower                                      |
| pickle_list          | 2.68 us                                                     | 2.82 us: 1.05x slower                                      |
| pickle               | 6.61 us                                                     | 6.98 us: 1.06x slower                                      |
| unpickle_list        | 2.55 us                                                     | 2.80 us: 1.10x slower                                      |
| Geometric mean       | (ref)                                                       | 1.02x faster                                               |

Benchmark hidden because not significant (3): pickle_dict, unpickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-pythonperf1-amd64-python-main-3.13.0a0-3a5be87 |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 18.7 ms                                                     | 19.0 ms: 1.01x slower                                      |
| python_startup_no_site | 15.9 ms                                                     | 16.3 ms: 1.03x slower                                      |
| Geometric mean         | (ref)                                                       | 1.02x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-pythonperf1-amd64-python-main-3.13.0a0-3a5be87 |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_xml     | 37.3 ms                                                     | 33.4 ms: 1.12x faster                                      |
| genshi_text    | 17.0 ms                                                     | 15.3 ms: 1.11x faster                                      |
| mako           | 7.26 ms                                                     | 6.62 ms: 1.10x faster                                      |
| Geometric mean | (ref)                                                       | 1.11x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230528-pythonperf1-amd64-python-main-3.13.0a0-3a5be87 |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 88.9 us: 3.62x faster                                      |
| generators               | 33.8 ms                                                     | 21.5 ms: 1.57x faster                                      |
| asyncio_tcp              | 699 ms                                                      | 485 ms: 1.44x faster                                       |
| json_dumps               | 7.56 ms                                                     | 5.64 ms: 1.34x faster                                      |
| richards_super           | 37.5 ms                                                     | 28.8 ms: 1.30x faster                                      |
| deltablue                | 2.61 ms                                                     | 2.08 ms: 1.25x faster                                      |
| richards                 | 30.6 ms                                                     | 25.0 ms: 1.22x faster                                      |
| sqlglot_parse            | 952 us                                                      | 785 us: 1.21x faster                                       |
| sqlglot_transpile        | 1.16 ms                                                     | 989 us: 1.18x faster                                       |
| hexiom                   | 4.55 ms                                                     | 3.92 ms: 1.16x faster                                      |
| logging_silent           | 69.8 ns                                                     | 60.3 ns: 1.16x faster                                      |
| unpickle_pure_python     | 152 us                                                      | 132 us: 1.15x faster                                       |
| comprehensions           | 15.9 us                                                     | 13.9 us: 1.14x faster                                      |
| raytrace                 | 211 ms                                                      | 186 ms: 1.13x faster                                       |
| go                       | 97.3 ms                                                     | 86.0 ms: 1.13x faster                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 1.87 sec: 1.13x faster                                     |
| json                     | 3.25 ms                                                     | 2.89 ms: 1.13x faster                                      |
| unpack_sequence          | 46.1 ns                                                     | 41.0 ns: 1.12x faster                                      |
| mdp                      | 1.67 sec                                                    | 1.49 sec: 1.12x faster                                     |
| genshi_xml               | 37.3 ms                                                     | 33.4 ms: 1.12x faster                                      |
| genshi_text              | 17.0 ms                                                     | 15.3 ms: 1.11x faster                                      |
| chaos                    | 47.1 ms                                                     | 42.7 ms: 1.10x faster                                      |
| mako                     | 7.26 ms                                                     | 6.62 ms: 1.10x faster                                      |
| scimark_lu               | 63.5 ms                                                     | 58.0 ms: 1.10x faster                                      |
| deepcopy_memo            | 25.2 us                                                     | 23.1 us: 1.09x faster                                      |
| async_tree_none          | 320 ms                                                      | 294 ms: 1.09x faster                                       |
| spectral_norm            | 67.9 ms                                                     | 62.4 ms: 1.09x faster                                      |
| async_tree_memoization   | 371 ms                                                      | 342 ms: 1.09x faster                                       |
| nqueens                  | 64.9 ms                                                     | 60.0 ms: 1.08x faster                                      |
| mypy2                    | 229 ms                                                      | 213 ms: 1.08x faster                                       |
| regex_compile            | 90.6 ms                                                     | 85.4 ms: 1.06x faster                                      |
| async_tree_io            | 779 ms                                                      | 734 ms: 1.06x faster                                       |
| coroutines               | 14.6 ms                                                     | 13.8 ms: 1.06x faster                                      |
| coverage                 | 55.9 ms                                                     | 52.7 ms: 1.06x faster                                      |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 473 ms: 1.06x faster                                       |
| pyflate                  | 304 ms                                                      | 288 ms: 1.06x faster                                       |
| tomli_loads              | 1.41 sec                                                    | 1.34 sec: 1.06x faster                                     |
| deepcopy                 | 246 us                                                      | 233 us: 1.05x faster                                       |
| pickle_pure_python       | 200 us                                                      | 190 us: 1.05x faster                                       |
| dulwich_log              | 44.5 ms                                                     | 42.3 ms: 1.05x faster                                      |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.45 ms: 1.05x faster                                      |
| sqlglot_normalize        | 190 ms                                                      | 181 ms: 1.05x faster                                       |
| fannkuch                 | 252 ms                                                      | 240 ms: 1.05x faster                                       |
| html5lib                 | 37.5 ms                                                     | 35.8 ms: 1.05x faster                                      |
| float                    | 54.6 ms                                                     | 52.2 ms: 1.05x faster                                      |
| logging_simple           | 6.61 us                                                     | 6.32 us: 1.05x faster                                      |
| pycparser                | 691 ms                                                      | 661 ms: 1.05x faster                                       |
| sqlglot_optimize         | 34.9 ms                                                     | 33.4 ms: 1.05x faster                                      |
| xml_etree_parse          | 95.9 ms                                                     | 91.7 ms: 1.05x faster                                      |
| logging_format           | 7.01 us                                                     | 6.73 us: 1.04x faster                                      |
| bench_thread_pool        | 852 us                                                      | 819 us: 1.04x faster                                       |
| meteor_contest           | 74.7 ms                                                     | 71.9 ms: 1.04x faster                                      |
| tornado_http             | 91.8 ms                                                     | 89.4 ms: 1.03x faster                                      |
| pprint_safe_repr         | 512 ms                                                      | 501 ms: 1.02x faster                                       |
| pprint_pformat           | 1.04 sec                                                    | 1.02 sec: 1.02x faster                                     |
| deepcopy_reduce          | 2.07 us                                                     | 2.05 us: 1.01x faster                                      |
| scimark_fft              | 178 ms                                                      | 180 ms: 1.01x slower                                       |
| xml_etree_iterparse      | 62.6 ms                                                     | 63.3 ms: 1.01x slower                                      |
| pidigits                 | 148 ms                                                      | 150 ms: 1.01x slower                                       |
| python_startup           | 18.7 ms                                                     | 19.0 ms: 1.01x slower                                      |
| python_startup_no_site   | 15.9 ms                                                     | 16.3 ms: 1.03x slower                                      |
| sqlite_synth             | 1.68 us                                                     | 1.73 us: 1.03x slower                                      |
| scimark_sor              | 75.6 ms                                                     | 77.7 ms: 1.03x slower                                      |
| regex_v8                 | 13.8 ms                                                     | 14.3 ms: 1.03x slower                                      |
| json_loads               | 12.9 us                                                     | 13.4 us: 1.04x slower                                      |
| xml_etree_generate       | 52.2 ms                                                     | 54.8 ms: 1.05x slower                                      |
| pickle_list              | 2.68 us                                                     | 2.82 us: 1.05x slower                                      |
| pickle                   | 6.61 us                                                     | 6.98 us: 1.06x slower                                      |
| regex_dna                | 115 ms                                                      | 124 ms: 1.07x slower                                       |
| bench_mp_pool            | 62.5 ms                                                     | 67.4 ms: 1.08x slower                                      |
| telco                    | 3.90 ms                                                     | 4.26 ms: 1.09x slower                                      |
| unpickle_list            | 2.55 us                                                     | 2.80 us: 1.10x slower                                      |
| regex_effbot             | 1.50 ms                                                     | 1.66 ms: 1.11x slower                                      |
| pathlib                  | 71.4 ms                                                     | 86.0 ms: 1.20x slower                                      |
| async_generators         | 178 ms                                                      | 237 ms: 1.33x slower                                       |
| Geometric mean           | (ref)                                                       | 1.07x faster                                               |

Benchmark hidden because not significant (9): pickle_dict, unpickle, crypto_pyaes, scimark_monte_carlo, xml_etree_process, create_gc_cycles, docutils, gc_traversal, nbody
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
