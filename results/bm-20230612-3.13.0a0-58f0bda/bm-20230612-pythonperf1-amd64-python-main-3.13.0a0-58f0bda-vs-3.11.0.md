
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 58f0bda
- commit date: 2023-06-12
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230612-pythonperf1-amd64-python-main-3.13.0a0-58f0bda |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| docutils       | 1.60 sec                                                    | 1.68 sec: 1.05x slower                                     |
| tornado_http   | 91.8 ms                                                     | 102 ms: 1.11x slower                                       |
| Geometric mean | (ref)                                                       | 1.08x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230612-pythonperf1-amd64-python-main-3.13.0a0-58f0bda |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 153 ms: 1.03x slower                                       |
| float          | 54.6 ms                                                     | 56.9 ms: 1.04x slower                                      |
| nbody          | 70.0 ms                                                     | 77.8 ms: 1.11x slower                                      |
| Geometric mean | (ref)                                                       | 1.06x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230612-pythonperf1-amd64-python-main-3.13.0a0-58f0bda |
|----------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 89.9 ms: 1.01x faster                                      |
| regex_v8       | 13.8 ms                                                     | 14.2 ms: 1.02x slower                                      |
| regex_dna      | 115 ms                                                      | 122 ms: 1.06x slower                                       |
| regex_effbot   | 1.50 ms                                                     | 1.64 ms: 1.09x slower                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230612-pythonperf1-amd64-python-main-3.13.0a0-58f0bda |
|----------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.76 ms: 1.31x faster                                      |
| unpickle_pure_python | 152 us                                                      | 143 us: 1.06x faster                                       |
| xml_etree_parse      | 95.9 ms                                                     | 94.5 ms: 1.02x faster                                      |
| pickle_pure_python   | 200 us                                                      | 202 us: 1.01x slower                                       |
| tomli_loads          | 1.41 sec                                                    | 1.48 sec: 1.04x slower                                     |
| unpickle             | 8.09 us                                                     | 8.49 us: 1.05x slower                                      |
| xml_etree_iterparse  | 62.6 ms                                                     | 67.1 ms: 1.07x slower                                      |
| json_loads           | 12.9 us                                                     | 13.9 us: 1.08x slower                                      |
| pickle               | 6.61 us                                                     | 7.14 us: 1.08x slower                                      |
| xml_etree_process    | 37.1 ms                                                     | 40.1 ms: 1.08x slower                                      |
| pickle_list          | 2.68 us                                                     | 2.93 us: 1.09x slower                                      |
| xml_etree_generate   | 52.2 ms                                                     | 58.0 ms: 1.11x slower                                      |
| unpickle_list        | 2.55 us                                                     | 2.89 us: 1.14x slower                                      |
| Geometric mean       | (ref)                                                       | 1.03x slower                                               |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230612-pythonperf1-amd64-python-main-3.13.0a0-58f0bda |
|------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 17.4 ms: 1.10x slower                                      |
| python_startup         | 18.7 ms                                                     | 20.7 ms: 1.11x slower                                      |
| Geometric mean         | (ref)                                                       | 1.10x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230612-pythonperf1-amd64-python-main-3.13.0a0-58f0bda |
|-----------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 7.56 ms: 1.04x slower                                      |

All benchmarks:
===============

| Benchmark                | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230612-pythonperf1-amd64-python-main-3.13.0a0-58f0bda |
|--------------------------|:-----------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 322 us                                                      | 95.5 us: 3.37x faster                                      |
| generators               | 33.8 ms                                                     | 23.2 ms: 1.46x faster                                      |
| json_dumps               | 7.56 ms                                                     | 5.76 ms: 1.31x faster                                      |
| richards_super           | 37.5 ms                                                     | 30.5 ms: 1.23x faster                                      |
| deltablue                | 2.61 ms                                                     | 2.18 ms: 1.20x faster                                      |
| richards                 | 30.6 ms                                                     | 27.1 ms: 1.13x faster                                      |
| unpack_sequence          | 46.1 ns                                                     | 40.9 ns: 1.13x faster                                      |
| sqlglot_parse            | 952 us                                                      | 848 us: 1.12x faster                                       |
| logging_silent           | 69.8 ns                                                     | 62.9 ns: 1.11x faster                                      |
| mdp                      | 1.67 sec                                                    | 1.51 sec: 1.11x faster                                     |
| json                     | 3.25 ms                                                     | 2.97 ms: 1.10x faster                                      |
| comprehensions           | 15.9 us                                                     | 14.5 us: 1.10x faster                                      |
| sqlglot_transpile        | 1.16 ms                                                     | 1.07 ms: 1.09x faster                                      |
| hexiom                   | 4.55 ms                                                     | 4.22 ms: 1.08x faster                                      |
| raytrace                 | 211 ms                                                      | 197 ms: 1.07x faster                                       |
| unpickle_pure_python     | 152 us                                                      | 143 us: 1.06x faster                                       |
| go                       | 97.3 ms                                                     | 91.9 ms: 1.06x faster                                      |
| chaos                    | 47.1 ms                                                     | 44.6 ms: 1.06x faster                                      |
| scimark_lu               | 63.5 ms                                                     | 60.5 ms: 1.05x faster                                      |
| spectral_norm            | 67.9 ms                                                     | 65.6 ms: 1.04x faster                                      |
| sqlglot_normalize        | 190 ms                                                      | 184 ms: 1.04x faster                                       |
| mypy2                    | 229 ms                                                      | 222 ms: 1.03x faster                                       |
| nqueens                  | 64.9 ms                                                     | 62.9 ms: 1.03x faster                                      |
| coverage                 | 55.9 ms                                                     | 54.7 ms: 1.02x faster                                      |
| deepcopy_memo            | 25.2 us                                                     | 24.6 us: 1.02x faster                                      |
| scimark_sparse_mat_mult  | 2.57 ms                                                     | 2.52 ms: 1.02x faster                                      |
| async_tree_none          | 320 ms                                                      | 315 ms: 1.02x faster                                       |
| xml_etree_parse          | 95.9 ms                                                     | 94.5 ms: 1.02x faster                                      |
| sqlglot_optimize         | 34.9 ms                                                     | 34.5 ms: 1.01x faster                                      |
| regex_compile            | 90.6 ms                                                     | 89.9 ms: 1.01x faster                                      |
| logging_simple           | 6.61 us                                                     | 6.67 us: 1.01x slower                                      |
| pickle_pure_python       | 200 us                                                      | 202 us: 1.01x slower                                       |
| crypto_pyaes             | 47.6 ms                                                     | 48.4 ms: 1.02x slower                                      |
| meteor_contest           | 74.7 ms                                                     | 76.5 ms: 1.02x slower                                      |
| regex_v8                 | 13.8 ms                                                     | 14.2 ms: 1.02x slower                                      |
| logging_format           | 7.01 us                                                     | 7.18 us: 1.02x slower                                      |
| async_tree_cpu_io_mixed  | 501 ms                                                      | 513 ms: 1.02x slower                                       |
| dulwich_log              | 44.5 ms                                                     | 45.8 ms: 1.03x slower                                      |
| pyflate                  | 304 ms                                                      | 313 ms: 1.03x slower                                       |
| pidigits                 | 148 ms                                                      | 153 ms: 1.03x slower                                       |
| coroutines               | 14.6 ms                                                     | 15.1 ms: 1.03x slower                                      |
| sqlite_synth             | 1.68 us                                                     | 1.75 us: 1.04x slower                                      |
| scimark_fft              | 178 ms                                                      | 186 ms: 1.04x slower                                       |
| mako                     | 7.26 ms                                                     | 7.56 ms: 1.04x slower                                      |
| pprint_safe_repr         | 512 ms                                                      | 533 ms: 1.04x slower                                       |
| float                    | 54.6 ms                                                     | 56.9 ms: 1.04x slower                                      |
| tomli_loads              | 1.41 sec                                                    | 1.48 sec: 1.04x slower                                     |
| scimark_monte_carlo      | 44.6 ms                                                     | 46.7 ms: 1.05x slower                                      |
| unpickle                 | 8.09 us                                                     | 8.49 us: 1.05x slower                                      |
| docutils                 | 1.60 sec                                                    | 1.68 sec: 1.05x slower                                     |
| pprint_pformat           | 1.04 sec                                                    | 1.10 sec: 1.06x slower                                     |
| deepcopy_reduce          | 2.07 us                                                     | 2.19 us: 1.06x slower                                      |
| fannkuch                 | 252 ms                                                      | 267 ms: 1.06x slower                                       |
| regex_dna                | 115 ms                                                      | 122 ms: 1.06x slower                                       |
| pycparser                | 691 ms                                                      | 734 ms: 1.06x slower                                       |
| gc_traversal             | 1.46 ms                                                     | 1.55 ms: 1.07x slower                                      |
| bench_thread_pool        | 852 us                                                      | 910 us: 1.07x slower                                       |
| telco                    | 3.90 ms                                                     | 4.18 ms: 1.07x slower                                      |
| xml_etree_iterparse      | 62.6 ms                                                     | 67.1 ms: 1.07x slower                                      |
| json_loads               | 12.9 us                                                     | 13.9 us: 1.08x slower                                      |
| pickle                   | 6.61 us                                                     | 7.14 us: 1.08x slower                                      |
| xml_etree_process        | 37.1 ms                                                     | 40.1 ms: 1.08x slower                                      |
| create_gc_cycles         | 693 us                                                      | 755 us: 1.09x slower                                       |
| pickle_list              | 2.68 us                                                     | 2.93 us: 1.09x slower                                      |
| regex_effbot             | 1.50 ms                                                     | 1.64 ms: 1.09x slower                                      |
| scimark_sor              | 75.6 ms                                                     | 82.9 ms: 1.10x slower                                      |
| python_startup_no_site   | 15.9 ms                                                     | 17.4 ms: 1.10x slower                                      |
| python_startup           | 18.7 ms                                                     | 20.7 ms: 1.11x slower                                      |
| asyncio_tcp_ssl          | 2.11 sec                                                    | 2.33 sec: 1.11x slower                                     |
| bench_mp_pool            | 62.5 ms                                                     | 69.2 ms: 1.11x slower                                      |
| tornado_http             | 91.8 ms                                                     | 102 ms: 1.11x slower                                       |
| nbody                    | 70.0 ms                                                     | 77.8 ms: 1.11x slower                                      |
| xml_etree_generate       | 52.2 ms                                                     | 58.0 ms: 1.11x slower                                      |
| unpickle_list            | 2.55 us                                                     | 2.89 us: 1.14x slower                                      |
| pathlib                  | 71.4 ms                                                     | 86.9 ms: 1.22x slower                                      |
| async_generators         | 178 ms                                                      | 248 ms: 1.40x slower                                       |
| Geometric mean           | (ref)                                                       | 1.01x faster                                               |

Benchmark hidden because not significant (5): asyncio_tcp, async_tree_memoization, deepcopy, pickle_dict, async_tree_io
Ignored benchmarks (17) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, dask, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
