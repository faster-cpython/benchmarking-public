# Results vs. 3.12.0

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: windows-amd64
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.07x faster
- HPT reliability: 98.63%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 231 ms: 1.06x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.76 sec: 1.06x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 86.3 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.03x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 186 ms: 1.53x faster                                                       |
| async_tree_memoization_tg  | 367 ms                                                      | 242 ms: 1.52x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 518 ms: 1.49x faster                                                       |
| async_tree_none            | 291 ms                                                      | 205 ms: 1.42x faster                                                       |
| async_tree_io              | 731 ms                                                      | 522 ms: 1.40x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 249 ms: 1.36x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 384 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 384 ms: 1.28x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.41x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 71.9 ms                                                     | 52.7 ms: 1.36x faster                                                      |
| float          | 56.8 ms                                                     | 45.0 ms: 1.26x faster                                                      |
| pidigits       | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                                      |
| regex_compile  | 87.5 ms                                                     | 89.0 ms: 1.02x slower                                                      |
| regex_v8       | 14.2 ms                                                     | 18.2 ms: 1.28x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 176 us: 1.11x faster                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.25 sec: 1.10x faster                                                     |
| xml_etree_iterparse  | 65.2 ms                                                     | 60.6 ms: 1.08x faster                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 52.4 ms: 1.07x faster                                                      |
| xml_etree_process    | 37.7 ms                                                     | 37.0 ms: 1.02x faster                                                      |
| unpickle_pure_python | 133 us                                                      | 132 us: 1.01x faster                                                       |
| json_dumps           | 5.70 ms                                                     | 5.75 ms: 1.01x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.5 us: 1.05x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.4 ms: 1.07x slower                                                      |
| python_startup         | 19.5 ms                                                     | 21.0 ms: 1.08x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 5.26 ms: 1.35x faster                                                      |
| django_template | 22.9 ms                                                     | 25.7 ms: 1.12x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.10x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none_tg         | 285 ms                                                      | 186 ms: 1.53x faster                                                       |
| deepcopy_memo              | 23.7 us                                                     | 15.6 us: 1.52x faster                                                      |
| async_tree_memoization_tg  | 367 ms                                                      | 242 ms: 1.52x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.39 sec: 1.51x faster                                                     |
| async_tree_io_tg           | 771 ms                                                      | 518 ms: 1.49x faster                                                       |
| spectral_norm              | 66.9 ms                                                     | 45.2 ms: 1.48x faster                                                      |
| async_tree_none            | 291 ms                                                      | 205 ms: 1.42x faster                                                       |
| async_tree_io              | 731 ms                                                      | 522 ms: 1.40x faster                                                       |
| comprehensions             | 14.1 us                                                     | 10.3 us: 1.38x faster                                                      |
| async_tree_memoization     | 339 ms                                                      | 249 ms: 1.36x faster                                                       |
| nbody                      | 71.9 ms                                                     | 52.7 ms: 1.36x faster                                                      |
| deepcopy                   | 238 us                                                      | 175 us: 1.36x faster                                                       |
| mako                       | 7.09 ms                                                     | 5.26 ms: 1.35x faster                                                      |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 384 ms: 1.31x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 384 ms: 1.28x faster                                                       |
| float                      | 56.8 ms                                                     | 45.0 ms: 1.26x faster                                                      |
| scimark_fft                | 184 ms                                                      | 150 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.14 ms: 1.19x faster                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 41.1 ms: 1.18x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.78 us: 1.18x faster                                                      |
| scimark_monte_carlo        | 43.7 ms                                                     | 37.6 ms: 1.16x faster                                                      |
| pyflate                    | 295 ms                                                      | 262 ms: 1.13x faster                                                       |
| pickle_pure_python         | 195 us                                                      | 176 us: 1.11x faster                                                       |
| pprint_safe_repr           | 513 ms                                                      | 465 ms: 1.10x faster                                                       |
| chaos                      | 43.3 ms                                                     | 39.3 ms: 1.10x faster                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.25 sec: 1.10x faster                                                     |
| pprint_pformat             | 1.05 sec                                                    | 957 ms: 1.09x faster                                                       |
| fannkuch                   | 247 ms                                                      | 226 ms: 1.09x faster                                                       |
| logging_simple             | 6.28 us                                                     | 5.77 us: 1.09x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 74.3 ms: 1.08x faster                                                      |
| logging_format             | 6.72 us                                                     | 6.21 us: 1.08x faster                                                      |
| raytrace                   | 192 ms                                                      | 178 ms: 1.08x faster                                                       |
| xml_etree_iterparse        | 65.2 ms                                                     | 60.6 ms: 1.08x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 798 us: 1.07x faster                                                       |
| regex_dna                  | 126 ms                                                      | 118 ms: 1.07x faster                                                       |
| xml_etree_generate         | 55.8 ms                                                     | 52.4 ms: 1.07x faster                                                      |
| logging_silent             | 60.5 ns                                                     | 56.9 ns: 1.06x faster                                                      |
| nqueens                    | 62.8 ms                                                     | 60.1 ms: 1.04x faster                                                      |
| coroutines                 | 14.3 ms                                                     | 13.7 ms: 1.04x faster                                                      |
| tornado_http               | 89.5 ms                                                     | 86.3 ms: 1.04x faster                                                      |
| asyncio_tcp                | 487 ms                                                      | 472 ms: 1.03x faster                                                       |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.03x faster                                                      |
| pidigits                   | 152 ms                                                      | 149 ms: 1.02x faster                                                       |
| xml_etree_process          | 37.7 ms                                                     | 37.0 ms: 1.02x faster                                                      |
| unpickle_pure_python       | 133 us                                                      | 132 us: 1.01x faster                                                       |
| meteor_contest             | 74.6 ms                                                     | 74.0 ms: 1.01x faster                                                      |
| sqlglot_parse              | 804 us                                                      | 800 us: 1.01x faster                                                       |
| sympy_sum                  | 91.5 ms                                                     | 92.2 ms: 1.01x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 5.75 ms: 1.01x slower                                                      |
| regex_compile              | 87.5 ms                                                     | 89.0 ms: 1.02x slower                                                      |
| sympy_str                  | 175 ms                                                      | 178 ms: 1.02x slower                                                       |
| go                         | 91.6 ms                                                     | 93.4 ms: 1.02x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 35.4 ms: 1.02x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.02x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.24 ms: 1.04x slower                                                      |
| generators                 | 22.5 ms                                                     | 23.4 ms: 1.04x slower                                                      |
| json_loads                 | 13.9 us                                                     | 14.5 us: 1.05x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.45 sec: 1.06x slower                                                     |
| docutils                   | 1.66 sec                                                    | 1.76 sec: 1.06x slower                                                     |
| 2to3                       | 218 ms                                                      | 231 ms: 1.06x slower                                                       |
| sympy_integrate            | 13.0 ms                                                     | 13.8 ms: 1.07x slower                                                      |
| telco                      | 4.13 ms                                                     | 4.42 ms: 1.07x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                     | 17.4 ms: 1.07x slower                                                      |
| python_startup             | 19.5 ms                                                     | 21.0 ms: 1.08x slower                                                      |
| sympy_expand               | 284 ms                                                      | 308 ms: 1.08x slower                                                       |
| async_generators           | 239 ms                                                      | 260 ms: 1.09x slower                                                       |
| richards                   | 28.4 ms                                                     | 31.0 ms: 1.09x slower                                                      |
| richards_super             | 32.1 ms                                                     | 35.1 ms: 1.09x slower                                                      |
| django_template            | 22.9 ms                                                     | 25.7 ms: 1.12x slower                                                      |
| coverage                   | 40.8 ms                                                     | 46.2 ms: 1.13x slower                                                      |
| hexiom                     | 4.10 ms                                                     | 4.65 ms: 1.13x slower                                                      |
| scimark_sor                | 78.8 ms                                                     | 89.5 ms: 1.14x slower                                                      |
| pycparser                  | 699 ms                                                      | 809 ms: 1.16x slower                                                       |
| typing_runtime_protocols   | 95.1 us                                                     | 113 us: 1.19x slower                                                       |
| create_gc_cycles           | 752 us                                                      | 900 us: 1.20x slower                                                       |
| scimark_lu                 | 58.9 ms                                                     | 73.0 ms: 1.24x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 18.2 ms: 1.28x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (5): xml_etree_parse, bench_mp_pool, sqlglot_transpile, sqlglot_normalize, json
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240708-3.14.0a0-006b53a-JIT/bm-20240708-pythonperf1-amd64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 98.63% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown