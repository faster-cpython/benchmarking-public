# Results vs. 3.12.0

- fork: python
- ref: c15f94d6fbc960790db3
- machine: windows-amd64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 208 ms: 1.05x faster                                                        |
| chameleon      | 4.98 ms                                                     | 4.81 ms: 1.04x faster                                                       |
| docutils       | 1.66 sec                                                    | 1.62 sec: 1.03x faster                                                      |
| tornado_http   | 89.5 ms                                                     | 82.1 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 258 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 204 ms: 1.40x faster                                                        |
| async_tree_none            | 291 ms                                                      | 217 ms: 1.34x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 384 ms: 1.31x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 265 ms: 1.28x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 605 ms: 1.28x faster                                                        |
| async_tree_io              | 731 ms                                                      | 580 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 389 ms: 1.26x faster                                                        |
| Geometric mean             | (ref)                                                       | 1.32x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 50.1 ms: 1.13x faster                                                       |
| nbody          | 71.9 ms                                                     | 64.9 ms: 1.11x faster                                                       |
| pidigits       | 152 ms                                                      | 150 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 78.1 ms: 1.12x faster                                                       |
| regex_dna      | 126 ms                                                      | 119 ms: 1.06x faster                                                        |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                       |
| regex_v8       | 14.2 ms                                                     | 17.6 ms: 1.23x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 172 us: 1.14x faster                                                        |
| unpickle_pure_python | 133 us                                                      | 124 us: 1.08x faster                                                        |
| pickle               | 7.43 us                                                     | 7.16 us: 1.04x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                     | 53.8 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.9 ms: 1.04x faster                                                       |
| unpickle_list        | 2.75 us                                                     | 2.70 us: 1.02x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.60 ms: 1.02x faster                                                       |
| xml_etree_process    | 37.7 ms                                                     | 37.1 ms: 1.02x faster                                                       |
| xml_etree_parse      | 93.0 ms                                                     | 92.1 ms: 1.01x faster                                                       |
| pickle_dict          | 18.4 us                                                     | 18.3 us: 1.01x faster                                                       |
| json_loads           | 13.9 us                                                     | 14.1 us: 1.02x slower                                                       |
| pickle_list          | 2.83 us                                                     | 2.89 us: 1.02x slower                                                       |
| unpickle             | 8.18 us                                                     | 8.45 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 16.6 ms: 1.02x slower                                                       |
| python_startup         | 19.5 ms                                                     | 20.2 ms: 1.04x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.41 ms: 1.10x faster                                                       |
| django_template | 22.9 ms                                                     | 22.6 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.06x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.46 sec: 1.44x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 258 ms: 1.42x faster                                                        |
| async_tree_none_tg         | 285 ms                                                      | 204 ms: 1.40x faster                                                        |
| comprehensions             | 14.1 us                                                     | 10.4 us: 1.36x faster                                                       |
| async_tree_none            | 291 ms                                                      | 217 ms: 1.34x faster                                                        |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 384 ms: 1.31x faster                                                        |
| async_tree_memoization     | 339 ms                                                      | 265 ms: 1.28x faster                                                        |
| async_tree_io_tg           | 771 ms                                                      | 605 ms: 1.28x faster                                                        |
| async_tree_io              | 731 ms                                                      | 580 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 389 ms: 1.26x faster                                                        |
| mypy2                      | 509 ms                                                      | 418 ms: 1.22x faster                                                        |
| raytrace                   | 192 ms                                                      | 159 ms: 1.21x faster                                                        |
| generators                 | 22.5 ms                                                     | 19.4 ms: 1.16x faster                                                       |
| dulwich_log                | 44.3 ms                                                     | 38.2 ms: 1.16x faster                                                       |
| logging_silent             | 60.5 ns                                                     | 52.6 ns: 1.15x faster                                                       |
| deltablue                  | 2.16 ms                                                     | 1.88 ms: 1.15x faster                                                       |
| chaos                      | 43.3 ms                                                     | 37.9 ms: 1.14x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 172 us: 1.14x faster                                                        |
| float                      | 56.8 ms                                                     | 50.1 ms: 1.13x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 55.9 ms: 1.12x faster                                                       |
| regex_compile              | 87.5 ms                                                     | 78.1 ms: 1.12x faster                                                       |
| nbody                      | 71.9 ms                                                     | 64.9 ms: 1.11x faster                                                       |
| mako                       | 7.09 ms                                                     | 6.41 ms: 1.10x faster                                                       |
| hexiom                     | 4.10 ms                                                     | 3.71 ms: 1.10x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.69 us: 1.10x faster                                                       |
| sqlite_synth               | 1.76 us                                                     | 1.60 us: 1.10x faster                                                       |
| go                         | 91.6 ms                                                     | 83.4 ms: 1.10x faster                                                       |
| sympy_str                  | 175 ms                                                      | 160 ms: 1.09x faster                                                        |
| tornado_http               | 89.5 ms                                                     | 82.1 ms: 1.09x faster                                                       |
| deepcopy                   | 238 us                                                      | 218 us: 1.09x faster                                                        |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.1 ms: 1.09x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 471 ms: 1.09x faster                                                        |
| logging_format             | 6.72 us                                                     | 6.17 us: 1.09x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 787 us: 1.09x faster                                                        |
| coroutines                 | 14.3 ms                                                     | 13.1 ms: 1.09x faster                                                       |
| sqlglot_normalize          | 187 ms                                                      | 172 ms: 1.08x faster                                                        |
| scimark_fft                | 184 ms                                                      | 170 ms: 1.08x faster                                                        |
| pprint_pformat             | 1.05 sec                                                    | 965 ms: 1.08x faster                                                        |
| crypto_pyaes               | 48.5 ms                                                     | 45.0 ms: 1.08x faster                                                       |
| unpickle_pure_python       | 133 us                                                      | 124 us: 1.08x faster                                                        |
| scimark_lu                 | 58.9 ms                                                     | 54.7 ms: 1.08x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 22.0 us: 1.08x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 85.3 ms: 1.07x faster                                                       |
| pathlib                    | 80.5 ms                                                     | 75.4 ms: 1.07x faster                                                       |
| scimark_sor                | 78.8 ms                                                     | 73.9 ms: 1.07x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.40 ms: 1.07x faster                                                       |
| sqlglot_parse              | 804 us                                                      | 755 us: 1.06x faster                                                        |
| bench_mp_pool              | 69.2 ms                                                     | 65.0 ms: 1.06x faster                                                       |
| async_generators           | 239 ms                                                      | 225 ms: 1.06x faster                                                        |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.06x faster                                                        |
| pyflate                    | 295 ms                                                      | 278 ms: 1.06x faster                                                        |
| sqlglot_transpile          | 1.02 ms                                                     | 964 us: 1.06x faster                                                        |
| deepcopy_reduce            | 2.09 us                                                     | 1.98 us: 1.06x faster                                                       |
| sympy_integrate            | 13.0 ms                                                     | 12.3 ms: 1.06x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 63.4 ms: 1.06x faster                                                       |
| sqlglot_optimize           | 34.5 ms                                                     | 32.8 ms: 1.05x faster                                                       |
| 2to3                       | 218 ms                                                      | 208 ms: 1.05x faster                                                        |
| sympy_expand               | 284 ms                                                      | 272 ms: 1.04x faster                                                        |
| richards_super             | 32.1 ms                                                     | 30.8 ms: 1.04x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 71.8 ms: 1.04x faster                                                       |
| richards                   | 28.4 ms                                                     | 27.3 ms: 1.04x faster                                                       |
| pickle                     | 7.43 us                                                     | 7.16 us: 1.04x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 53.8 ms: 1.04x faster                                                       |
| json                       | 3.05 ms                                                     | 2.94 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.9 ms: 1.04x faster                                                       |
| chameleon                  | 4.98 ms                                                     | 4.81 ms: 1.04x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                       |
| docutils                   | 1.66 sec                                                    | 1.62 sec: 1.03x faster                                                      |
| unpickle_list              | 2.75 us                                                     | 2.70 us: 1.02x faster                                                       |
| json_dumps                 | 5.70 ms                                                     | 5.60 ms: 1.02x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 37.1 ms: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 150 ms: 1.02x faster                                                        |
| django_template            | 22.9 ms                                                     | 22.6 ms: 1.01x faster                                                       |
| xml_etree_parse            | 93.0 ms                                                     | 92.1 ms: 1.01x faster                                                       |
| fannkuch                   | 247 ms                                                      | 244 ms: 1.01x faster                                                        |
| pickle_dict                | 18.4 us                                                     | 18.3 us: 1.01x faster                                                       |
| json_loads                 | 13.9 us                                                     | 14.1 us: 1.02x slower                                                       |
| aiohttp                    | 884 us                                                      | 898 us: 1.02x slower                                                        |
| python_startup_no_site     | 16.2 ms                                                     | 16.6 ms: 1.02x slower                                                       |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                       |
| pickle_list                | 2.83 us                                                     | 2.89 us: 1.02x slower                                                       |
| unpickle                   | 8.18 us                                                     | 8.45 us: 1.03x slower                                                       |
| python_startup             | 19.5 ms                                                     | 20.2 ms: 1.04x slower                                                       |
| coverage                   | 40.8 ms                                                     | 43.3 ms: 1.06x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 102 us: 1.08x slower                                                        |
| pycparser                  | 699 ms                                                      | 786 ms: 1.13x slower                                                        |
| telco                      | 4.13 ms                                                     | 4.68 ms: 1.13x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 900 us: 1.20x slower                                                        |
| regex_v8                   | 14.2 ms                                                     | 17.6 ms: 1.23x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (3): asyncio_tcp, tomli_loads, mdp
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240608-3.13.0b2+-c15f94d/bm-20240608-pythonperf1-amd64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: unknown