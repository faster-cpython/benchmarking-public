# Results vs. 3.12.0

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: windows-amd64
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.07x faster
- HPT reliability: 98.20%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 232 ms: 1.06x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.75 sec: 1.05x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 83.8 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 185 ms: 1.54x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 243 ms: 1.51x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 523 ms: 1.48x faster                                                       |
| async_tree_none            | 291 ms                                                      | 205 ms: 1.42x faster                                                       |
| async_tree_io              | 731 ms                                                      | 530 ms: 1.38x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 251 ms: 1.35x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 383 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 381 ms: 1.28x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.41x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 53.4 ms: 1.35x faster                                                      |
| float          | 56.8 ms                                                     | 45.0 ms: 1.26x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.20x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 122 ms: 1.04x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 89.1 ms: 1.02x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 16.1 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 174 us: 1.12x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.23 sec: 1.11x faster                                                     |
| xml_etree_iterparse  | 65.2 ms                                                     | 60.7 ms: 1.07x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 52.2 ms: 1.07x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 36.7 ms: 1.03x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 130 us: 1.02x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.79 ms: 1.02x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.5 ms: 1.08x slower                                                      |
| python_startup         | 19.5 ms                                                     | 21.0 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.17 ms: 1.37x faster                                                      |
| django_template | 22.9 ms                                                     | 26.1 ms: 1.14x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 185 ms: 1.54x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 15.5 us: 1.53x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 243 ms: 1.51x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 44.5 ms: 1.50x faster                                                      |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.41 sec: 1.48x faster                                                     |
| async_tree_io_tg           | 771 ms                                                      | 523 ms: 1.48x faster                                                       |
| async_tree_none            | 291 ms                                                      | 205 ms: 1.42x faster                                                       |
| async_tree_io              | 731 ms                                                      | 530 ms: 1.38x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.3 us: 1.37x faster                                                      |
| mako                       | 7.09 ms                                                     | 5.17 ms: 1.37x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 251 ms: 1.35x faster                                                       |
| deepcopy                   | 238 us                                                      | 177 us: 1.35x faster                                                       |
| nbody                      | 71.9 ms                                                     | 53.4 ms: 1.35x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 383 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 381 ms: 1.28x faster                                                       |
| float                      | 56.8 ms                                                     | 45.0 ms: 1.26x faster                                                      |
| scimark_fft                | 184 ms                                                      | 150 ms: 1.23x faster                                                       |
| crypto_pyaes               | 48.5 ms                                                     | 40.2 ms: 1.21x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.76 us: 1.19x faster                                                      |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.18 ms: 1.17x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 37.6 ms: 1.16x faster                                                      |
| pyflate                    | 295 ms                                                      | 256 ms: 1.15x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 174 us: 1.12x faster                                                       |
| chaos                      | 43.3 ms                                                     | 38.8 ms: 1.12x faster                                                      |
| logging_simple             | 6.28 us                                                     | 5.63 us: 1.11x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.23 sec: 1.11x faster                                                     |
| fannkuch                   | 247 ms                                                      | 222 ms: 1.11x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 464 ms: 1.11x faster                                                       |
| logging_format             | 6.72 us                                                     | 6.08 us: 1.11x faster                                                      |
| pprint_pformat             | 1.05 sec                                                    | 950 ms: 1.10x faster                                                       |
| raytrace                   | 192 ms                                                      | 176 ms: 1.09x faster                                                       |
| bench_thread_pool          | 857 us                                                      | 797 us: 1.07x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 60.7 ms: 1.07x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 56.5 ns: 1.07x faster                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 52.2 ms: 1.07x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 83.8 ms: 1.07x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 75.5 ms: 1.07x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 465 ms: 1.05x faster                                                       |
| regex_dna                  | 126 ms                                                      | 122 ms: 1.04x faster                                                       |
| nqueens                    | 62.8 ms                                                     | 60.5 ms: 1.04x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.9 ms: 1.03x faster                                                      |
| xml_etree_process          | 37.7 ms                                                     | 36.7 ms: 1.03x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 130 us: 1.02x faster                                                       |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 73.2 ms: 1.02x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                      |
| sqlglot_parse              | 804 us                                                      | 800 us: 1.01x faster                                                       |
| sqlglot_normalize          | 187 ms                                                      | 188 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.02 ms                                                     | 1.03 ms: 1.01x slower                                                      |
| sympy_sum                  | 91.5 ms                                                     | 92.6 ms: 1.01x slower                                                      |
| go                         | 91.6 ms                                                     | 93.0 ms: 1.02x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.79 ms: 1.02x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 89.1 ms: 1.02x slower                                                      |
| sympy_str                  | 175 ms                                                      | 179 ms: 1.02x slower                                                       |
| json_loads                 | 13.9 us                                                     | 14.2 us: 1.02x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.41 sec: 1.03x slower                                                     |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.03x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 35.5 ms: 1.03x slower                                                      |
| generators                 | 22.5 ms                                                     | 23.5 ms: 1.04x slower                                                      |
| richards_super             | 32.1 ms                                                     | 33.6 ms: 1.05x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.26 ms: 1.05x slower                                                      |
| richards                   | 28.4 ms                                                     | 29.8 ms: 1.05x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.75 sec: 1.05x slower                                                     |
| async_generators           | 239 ms                                                      | 253 ms: 1.06x slower                                                       |
| 2to3                       | 218 ms                                                      | 232 ms: 1.06x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.8 ms: 1.07x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 17.5 ms: 1.08x slower                                                      |
| python_startup             | 19.5 ms                                                     | 21.0 ms: 1.08x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.49 ms: 1.09x slower                                                      |
| sympy_expand               | 284 ms                                                      | 310 ms: 1.09x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 86.5 ms: 1.10x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.61 ms: 1.12x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 16.1 ms: 1.13x slower                                                      |
| django_template            | 22.9 ms                                                     | 26.1 ms: 1.14x slower                                                      |
| coverage                   | 40.8 ms                                                     | 46.5 ms: 1.14x slower                                                      |
| pycparser                  | 699 ms                                                      | 811 ms: 1.16x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 898 us: 1.19x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 115 us: 1.21x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 74.6 ms: 1.27x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (3): xml_etree_parse, bench_mp_pool, json
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240708-3.14.0a0-006b53a-JIT/bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 98.20% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown