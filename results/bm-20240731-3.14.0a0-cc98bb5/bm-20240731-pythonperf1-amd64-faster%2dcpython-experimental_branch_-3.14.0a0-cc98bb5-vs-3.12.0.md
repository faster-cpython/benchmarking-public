# Results vs. 3.12.0

- fork: faster-cpython
- ref: experimental_branch_
- machine: windows-amd64
- commit hash: cc98bb5
- commit date: 2024-07-31
- overall geometric mean: 1.02x slower
- HPT reliability: 99.96%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 230 ms: 1.05x slower                                                                 |
| docutils       | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                               |
| tornado_http   | 89.5 ms                                                     | 92.6 ms: 1.03x slower                                                                |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 247 ms: 1.49x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 195 ms: 1.46x faster                                                                 |
| async_tree_io_tg           | 771 ms                                                      | 540 ms: 1.43x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 217 ms: 1.34x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 386 ms: 1.30x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 264 ms: 1.28x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 384 ms: 1.27x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 583 ms: 1.25x faster                                                                 |
| Geometric mean             | (ref)                                                       | 1.35x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 55.9 ms: 1.02x faster                                                                |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                                 |
| nbody          | 71.9 ms                                                     | 85.4 ms: 1.19x slower                                                                |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 123 ms: 1.03x faster                                                                 |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.01x faster                                                                |
| regex_compile  | 87.5 ms                                                     | 91.8 ms: 1.05x slower                                                                |
| regex_v8       | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                                |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads           | 13.9 us                                                     | 14.3 us: 1.03x slower                                                                |
| xml_etree_generate   | 55.8 ms                                                     | 58.4 ms: 1.05x slower                                                                |
| xml_etree_process    | 37.7 ms                                                     | 41.1 ms: 1.09x slower                                                                |
| json_dumps           | 5.70 ms                                                     | 6.22 ms: 1.09x slower                                                                |
| pickle_pure_python   | 195 us                                                      | 214 us: 1.10x slower                                                                 |
| tomli_loads          | 1.37 sec                                                    | 1.54 sec: 1.12x slower                                                               |
| unpickle_pure_python | 133 us                                                      | 153 us: 1.15x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.07x slower                                                                         |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.7 ms: 1.09x slower                                                                |
| python_startup         | 19.5 ms                                                     | 21.5 ms: 1.10x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 24.8 ms: 1.08x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                                         |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 247 ms: 1.49x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 195 ms: 1.46x faster                                                                 |
| async_tree_io_tg           | 771 ms                                                      | 540 ms: 1.43x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 217 ms: 1.34x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 386 ms: 1.30x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 264 ms: 1.28x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 384 ms: 1.27x faster                                                                 |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.65 sec: 1.27x faster                                                               |
| deepcopy                   | 238 us                                                      | 189 us: 1.26x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 583 ms: 1.25x faster                                                                 |
| comprehensions             | 14.1 us                                                     | 12.4 us: 1.14x faster                                                                |
| deepcopy_memo              | 23.7 us                                                     | 20.9 us: 1.13x faster                                                                |
| deepcopy_reduce            | 2.09 us                                                     | 1.94 us: 1.08x faster                                                                |
| bench_thread_pool          | 857 us                                                      | 808 us: 1.06x faster                                                                 |
| generators                 | 22.5 ms                                                     | 21.5 ms: 1.05x faster                                                                |
| regex_dna                  | 126 ms                                                      | 123 ms: 1.03x faster                                                                 |
| dulwich_log                | 44.3 ms                                                     | 43.1 ms: 1.03x faster                                                                |
| coroutines                 | 14.3 ms                                                     | 14.0 ms: 1.02x faster                                                                |
| float                      | 56.8 ms                                                     | 55.9 ms: 1.02x faster                                                                |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.01x faster                                                                |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                                 |
| raytrace                   | 192 ms                                                      | 192 ms: 1.00x faster                                                                 |
| async_generators           | 239 ms                                                      | 243 ms: 1.01x slower                                                                 |
| logging_simple             | 6.28 us                                                     | 6.41 us: 1.02x slower                                                                |
| gc_traversal               | 1.52 ms                                                     | 1.56 ms: 1.02x slower                                                                |
| json_loads                 | 13.9 us                                                     | 14.3 us: 1.03x slower                                                                |
| sympy_str                  | 175 ms                                                      | 180 ms: 1.03x slower                                                                 |
| json                       | 3.05 ms                                                     | 3.14 ms: 1.03x slower                                                                |
| sympy_integrate            | 13.0 ms                                                     | 13.4 ms: 1.03x slower                                                                |
| tornado_http               | 89.5 ms                                                     | 92.6 ms: 1.03x slower                                                                |
| chaos                      | 43.3 ms                                                     | 45.0 ms: 1.04x slower                                                                |
| meteor_contest             | 74.6 ms                                                     | 77.5 ms: 1.04x slower                                                                |
| logging_format             | 6.72 us                                                     | 6.98 us: 1.04x slower                                                                |
| deltablue                  | 2.16 ms                                                     | 2.26 ms: 1.05x slower                                                                |
| xml_etree_generate         | 55.8 ms                                                     | 58.4 ms: 1.05x slower                                                                |
| nqueens                    | 62.8 ms                                                     | 65.7 ms: 1.05x slower                                                                |
| sqlglot_normalize          | 187 ms                                                      | 196 ms: 1.05x slower                                                                 |
| regex_compile              | 87.5 ms                                                     | 91.8 ms: 1.05x slower                                                                |
| docutils                   | 1.66 sec                                                    | 1.74 sec: 1.05x slower                                                               |
| mdp                        | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                               |
| logging_silent             | 60.5 ns                                                     | 63.6 ns: 1.05x slower                                                                |
| sqlglot_optimize           | 34.5 ms                                                     | 36.3 ms: 1.05x slower                                                                |
| 2to3                       | 218 ms                                                      | 230 ms: 1.05x slower                                                                 |
| spectral_norm              | 66.9 ms                                                     | 71.8 ms: 1.07x slower                                                                |
| crypto_pyaes               | 48.5 ms                                                     | 52.2 ms: 1.08x slower                                                                |
| django_template            | 22.9 ms                                                     | 24.8 ms: 1.08x slower                                                                |
| pycparser                  | 699 ms                                                      | 755 ms: 1.08x slower                                                                 |
| sympy_expand               | 284 ms                                                      | 309 ms: 1.09x slower                                                                 |
| regex_v8                   | 14.2 ms                                                     | 15.5 ms: 1.09x slower                                                                |
| xml_etree_process          | 37.7 ms                                                     | 41.1 ms: 1.09x slower                                                                |
| python_startup_no_site     | 16.2 ms                                                     | 17.7 ms: 1.09x slower                                                                |
| json_dumps                 | 5.70 ms                                                     | 6.22 ms: 1.09x slower                                                                |
| go                         | 91.6 ms                                                     | 99.9 ms: 1.09x slower                                                                |
| sqlglot_transpile          | 1.02 ms                                                     | 1.12 ms: 1.09x slower                                                                |
| asyncio_tcp                | 487 ms                                                      | 534 ms: 1.10x slower                                                                 |
| pickle_pure_python         | 195 us                                                      | 214 us: 1.10x slower                                                                 |
| pprint_safe_repr           | 513 ms                                                      | 564 ms: 1.10x slower                                                                 |
| pprint_pformat             | 1.05 sec                                                    | 1.15 sec: 1.10x slower                                                               |
| python_startup             | 19.5 ms                                                     | 21.5 ms: 1.10x slower                                                                |
| richards                   | 28.4 ms                                                     | 31.5 ms: 1.11x slower                                                                |
| richards_super             | 32.1 ms                                                     | 35.7 ms: 1.11x slower                                                                |
| pyflate                    | 295 ms                                                      | 328 ms: 1.11x slower                                                                 |
| sqlglot_parse              | 804 us                                                      | 897 us: 1.11x slower                                                                 |
| scimark_lu                 | 58.9 ms                                                     | 65.8 ms: 1.12x slower                                                                |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.87 ms: 1.12x slower                                                                |
| tomli_loads                | 1.37 sec                                                    | 1.54 sec: 1.12x slower                                                               |
| hexiom                     | 4.10 ms                                                     | 4.62 ms: 1.13x slower                                                                |
| scimark_fft                | 184 ms                                                      | 208 ms: 1.13x slower                                                                 |
| unpickle_pure_python       | 133 us                                                      | 153 us: 1.15x slower                                                                 |
| nbody                      | 71.9 ms                                                     | 85.4 ms: 1.19x slower                                                                |
| coverage                   | 40.8 ms                                                     | 48.7 ms: 1.19x slower                                                                |
| scimark_sor                | 78.8 ms                                                     | 94.3 ms: 1.20x slower                                                                |
| create_gc_cycles           | 752 us                                                      | 902 us: 1.20x slower                                                                 |
| typing_runtime_protocols   | 95.1 us                                                     | 114 us: 1.20x slower                                                                 |
| scimark_monte_carlo        | 43.7 ms                                                     | 52.7 ms: 1.20x slower                                                                |
| telco                      | 4.13 ms                                                     | 5.05 ms: 1.22x slower                                                                |
| fannkuch                   | 247 ms                                                      | 302 ms: 1.22x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                         |

Benchmark hidden because not significant (6): mako, sympy_sum, xml_etree_parse, pathlib, bench_mp_pool, xml_etree_iterparse
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240731-3.14.0a0-cc98bb5/bm-20240731-pythonperf1-amd64-faster%2dcpython-experimental_branch_-3.14.0a0-cc98bb5.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown