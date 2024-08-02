# Results vs. 3.12.0

- fork: mdboom
- ref: remove_pragma_313
- machine: windows-amd64
- commit hash: 3fbe4c2
- commit date: 2024-07-02
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3+-3fbe4c2 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 213 ms: 1.02x faster                                                     |
| chameleon      | 4.98 ms                                                     | 4.68 ms: 1.06x faster                                                    |
| docutils       | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                   |
| tornado_http   | 89.5 ms                                                     | 82.4 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                       | 1.05x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3+-3fbe4c2 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 261 ms: 1.40x faster                                                     |
| async_tree_none_tg         | 285 ms                                                      | 205 ms: 1.39x faster                                                     |
| async_tree_none            | 291 ms                                                      | 217 ms: 1.34x faster                                                     |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 381 ms: 1.32x faster                                                     |
| async_tree_memoization     | 339 ms                                                      | 267 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 385 ms: 1.27x faster                                                     |
| async_tree_io_tg           | 771 ms                                                      | 607 ms: 1.27x faster                                                     |
| async_tree_io              | 731 ms                                                      | 586 ms: 1.25x faster                                                     |
| Geometric mean             | (ref)                                                       | 1.31x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3+-3fbe4c2 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 50.0 ms: 1.14x faster                                                    |
| nbody          | 71.9 ms                                                     | 69.0 ms: 1.04x faster                                                    |
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                       | 1.06x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3+-3fbe4c2 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 87.5 ms                                                     | 81.4 ms: 1.08x faster                                                    |
| regex_dna      | 126 ms                                                      | 120 ms: 1.06x faster                                                     |
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                    |
| regex_v8       | 14.2 ms                                                     | 16.4 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                       | 1.00x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3+-3fbe4c2 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 195 us                                                      | 181 us: 1.08x faster                                                     |
| unpickle_pure_python | 133 us                                                      | 124 us: 1.07x faster                                                     |
| xml_etree_generate   | 55.8 ms                                                     | 53.9 ms: 1.04x faster                                                    |
| xml_etree_iterparse  | 65.2 ms                                                     | 62.9 ms: 1.04x faster                                                    |
| xml_etree_process    | 37.7 ms                                                     | 36.7 ms: 1.03x faster                                                    |
| json_loads           | 13.9 us                                                     | 14.4 us: 1.04x slower                                                    |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                             |

Benchmark hidden because not significant (3): xml_etree_parse, json_dumps, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3+-3fbe4c2 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.1 ms: 1.05x slower                                                    |
| python_startup         | 19.5 ms                                                     | 20.7 ms: 1.07x slower                                                    |
| Geometric mean         | (ref)                                                       | 1.06x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3+-3fbe4c2 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                     | 6.38 ms: 1.11x faster                                                    |
| django_template | 22.9 ms                                                     | 21.9 ms: 1.05x faster                                                    |
| Geometric mean  | (ref)                                                       | 1.08x faster                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3+-3fbe4c2 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------:|
| comprehensions             | 14.1 us                                                     | 9.95 us: 1.42x faster                                                    |
| async_tree_memoization_tg  | 367 ms                                                      | 261 ms: 1.40x faster                                                     |
| async_tree_none_tg         | 285 ms                                                      | 205 ms: 1.39x faster                                                     |
| async_tree_none            | 291 ms                                                      | 217 ms: 1.34x faster                                                     |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.56 sec: 1.34x faster                                                   |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 381 ms: 1.32x faster                                                     |
| async_tree_memoization     | 339 ms                                                      | 267 ms: 1.27x faster                                                     |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 385 ms: 1.27x faster                                                     |
| async_tree_io_tg           | 771 ms                                                      | 607 ms: 1.27x faster                                                     |
| async_tree_io              | 731 ms                                                      | 586 ms: 1.25x faster                                                     |
| raytrace                   | 192 ms                                                      | 158 ms: 1.22x faster                                                     |
| mypy2                      | 509 ms                                                      | 429 ms: 1.19x faster                                                     |
| logging_silent             | 60.5 ns                                                     | 52.2 ns: 1.16x faster                                                    |
| chaos                      | 43.3 ms                                                     | 37.9 ms: 1.14x faster                                                    |
| float                      | 56.8 ms                                                     | 50.0 ms: 1.14x faster                                                    |
| generators                 | 22.5 ms                                                     | 19.9 ms: 1.13x faster                                                    |
| bench_thread_pool          | 857 us                                                      | 761 us: 1.12x faster                                                     |
| deltablue                  | 2.16 ms                                                     | 1.93 ms: 1.12x faster                                                    |
| hexiom                     | 4.10 ms                                                     | 3.68 ms: 1.11x faster                                                    |
| nqueens                    | 62.8 ms                                                     | 56.5 ms: 1.11x faster                                                    |
| mako                       | 7.09 ms                                                     | 6.38 ms: 1.11x faster                                                    |
| logging_simple             | 6.28 us                                                     | 5.68 us: 1.10x faster                                                    |
| logging_format             | 6.72 us                                                     | 6.12 us: 1.10x faster                                                    |
| coroutines                 | 14.3 ms                                                     | 13.0 ms: 1.09x faster                                                    |
| dulwich_log                | 44.3 ms                                                     | 40.5 ms: 1.09x faster                                                    |
| tornado_http               | 89.5 ms                                                     | 82.4 ms: 1.09x faster                                                    |
| deepcopy                   | 238 us                                                      | 219 us: 1.09x faster                                                     |
| scimark_monte_carlo        | 43.7 ms                                                     | 40.3 ms: 1.09x faster                                                    |
| sqlglot_normalize          | 187 ms                                                      | 172 ms: 1.08x faster                                                     |
| pickle_pure_python         | 195 us                                                      | 181 us: 1.08x faster                                                     |
| go                         | 91.6 ms                                                     | 84.8 ms: 1.08x faster                                                    |
| crypto_pyaes               | 48.5 ms                                                     | 45.1 ms: 1.08x faster                                                    |
| regex_compile              | 87.5 ms                                                     | 81.4 ms: 1.08x faster                                                    |
| deepcopy_memo              | 23.7 us                                                     | 22.1 us: 1.07x faster                                                    |
| unpickle_pure_python       | 133 us                                                      | 124 us: 1.07x faster                                                     |
| scimark_lu                 | 58.9 ms                                                     | 55.1 ms: 1.07x faster                                                    |
| sympy_sum                  | 91.5 ms                                                     | 86.0 ms: 1.06x faster                                                    |
| richards_super             | 32.1 ms                                                     | 30.2 ms: 1.06x faster                                                    |
| chameleon                  | 4.98 ms                                                     | 4.68 ms: 1.06x faster                                                    |
| spectral_norm              | 66.9 ms                                                     | 63.0 ms: 1.06x faster                                                    |
| scimark_fft                | 184 ms                                                      | 174 ms: 1.06x faster                                                     |
| pprint_safe_repr           | 513 ms                                                      | 483 ms: 1.06x faster                                                     |
| pprint_pformat             | 1.05 sec                                                    | 987 ms: 1.06x faster                                                     |
| deepcopy_reduce            | 2.09 us                                                     | 1.98 us: 1.06x faster                                                    |
| richards                   | 28.4 ms                                                     | 26.8 ms: 1.06x faster                                                    |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.06x faster                                                     |
| pyflate                    | 295 ms                                                      | 280 ms: 1.05x faster                                                     |
| bench_mp_pool              | 69.2 ms                                                     | 65.7 ms: 1.05x faster                                                    |
| pycparser                  | 699 ms                                                      | 665 ms: 1.05x faster                                                     |
| pathlib                    | 80.5 ms                                                     | 76.7 ms: 1.05x faster                                                    |
| sympy_integrate            | 13.0 ms                                                     | 12.4 ms: 1.05x faster                                                    |
| sympy_str                  | 175 ms                                                      | 167 ms: 1.05x faster                                                     |
| django_template            | 22.9 ms                                                     | 21.9 ms: 1.05x faster                                                    |
| scimark_sor                | 78.8 ms                                                     | 75.3 ms: 1.05x faster                                                    |
| async_generators           | 239 ms                                                      | 229 ms: 1.04x faster                                                     |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.45 ms: 1.04x faster                                                    |
| nbody                      | 71.9 ms                                                     | 69.0 ms: 1.04x faster                                                    |
| sqlglot_transpile          | 1.02 ms                                                     | 982 us: 1.04x faster                                                     |
| xml_etree_generate         | 55.8 ms                                                     | 53.9 ms: 1.04x faster                                                    |
| meteor_contest             | 74.6 ms                                                     | 72.0 ms: 1.04x faster                                                    |
| xml_etree_iterparse        | 65.2 ms                                                     | 62.9 ms: 1.04x faster                                                    |
| sqlglot_parse              | 804 us                                                      | 780 us: 1.03x faster                                                     |
| asyncio_tcp                | 487 ms                                                      | 474 ms: 1.03x faster                                                     |
| xml_etree_process          | 37.7 ms                                                     | 36.7 ms: 1.03x faster                                                    |
| 2to3                       | 218 ms                                                      | 213 ms: 1.02x faster                                                     |
| json                       | 3.05 ms                                                     | 2.98 ms: 1.02x faster                                                    |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                                    |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                     |
| docutils                   | 1.66 sec                                                    | 1.64 sec: 1.01x faster                                                   |
| fannkuch                   | 247 ms                                                      | 248 ms: 1.01x slower                                                     |
| sympy_expand               | 284 ms                                                      | 286 ms: 1.01x slower                                                     |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                    |
| json_loads                 | 13.9 us                                                     | 14.4 us: 1.04x slower                                                    |
| python_startup_no_site     | 16.2 ms                                                     | 17.1 ms: 1.05x slower                                                    |
| python_startup             | 19.5 ms                                                     | 20.7 ms: 1.07x slower                                                    |
| typing_runtime_protocols   | 95.1 us                                                     | 103 us: 1.08x slower                                                     |
| coverage                   | 40.8 ms                                                     | 45.7 ms: 1.12x slower                                                    |
| telco                      | 4.13 ms                                                     | 4.68 ms: 1.13x slower                                                    |
| regex_v8                   | 14.2 ms                                                     | 16.4 ms: 1.15x slower                                                    |
| create_gc_cycles           | 752 us                                                      | 901 us: 1.20x slower                                                     |
| Geometric mean             | (ref)                                                       | 1.07x faster                                                             |

Benchmark hidden because not significant (5): sqlglot_optimize, xml_etree_parse, json_dumps, tomli_loads, mdp
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240702-3.13.0b3+-3fbe4c2/bm-20240702-pythonperf1-amd64-mdboom-remove_pragma_313-3.13.0b3+-3fbe4c2.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown