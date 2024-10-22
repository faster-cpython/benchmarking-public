# Results vs. 3.12.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: windows-amd64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.01x slower
- HPT reliability: 99.68%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 223 ms: 1.02x slower                                                       |
| docutils       | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                     |
| tornado_http   | 89.5 ms                                                     | 92.2 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 254 ms: 1.44x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 201 ms: 1.42x faster                                                       |
| async_tree_none            | 291 ms                                                      | 209 ms: 1.39x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 565 ms: 1.37x faster                                                       |
| async_tree_memoization     | 339 ms                                                      | 261 ms: 1.30x faster                                                       |
| async_tree_io              | 731 ms                                                      | 574 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 397 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 389 ms: 1.26x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.34x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 56.8 ms                                                     | 55.9 ms: 1.02x faster                                                      |
| pidigits       | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| nbody          | 71.9 ms                                                     | 82.0 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                       | 1.04x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 119 ms: 1.07x faster                                                       |
| regex_effbot   | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| regex_v8       | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                      |
| regex_compile  | 87.5 ms                                                     | 91.4 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                       | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle               | 7.43 us                                                     | 7.27 us: 1.02x faster                                                      |
| xml_etree_parse      | 93.0 ms                                                     | 94.0 ms: 1.01x slower                                                      |
| unpickle_list        | 2.75 us                                                     | 2.80 us: 1.02x slower                                                      |
| pickle_dict          | 18.4 us                                                     | 18.9 us: 1.03x slower                                                      |
| xml_etree_generate   | 55.8 ms                                                     | 57.6 ms: 1.03x slower                                                      |
| pickle_list          | 2.83 us                                                     | 2.95 us: 1.04x slower                                                      |
| json_loads           | 13.9 us                                                     | 14.7 us: 1.05x slower                                                      |
| json_dumps           | 5.70 ms                                                     | 6.19 ms: 1.09x slower                                                      |
| xml_etree_process    | 37.7 ms                                                     | 41.0 ms: 1.09x slower                                                      |
| pickle_pure_python   | 195 us                                                      | 213 us: 1.09x slower                                                       |
| unpickle             | 8.18 us                                                     | 9.04 us: 1.10x slower                                                      |
| unpickle_pure_python | 133 us                                                      | 148 us: 1.11x slower                                                       |
| tomli_loads          | 1.37 sec                                                    | 1.59 sec: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.7 ms: 1.09x slower                                                      |
| python_startup         | 19.5 ms                                                     | 21.9 ms: 1.13x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 25.1 ms: 1.09x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 254 ms: 1.44x faster                                                       |
| async_tree_none_tg         | 285 ms                                                      | 201 ms: 1.42x faster                                                       |
| async_tree_none            | 291 ms                                                      | 209 ms: 1.39x faster                                                       |
| async_tree_io_tg           | 771 ms                                                      | 565 ms: 1.37x faster                                                       |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.58 sec: 1.32x faster                                                     |
| async_tree_memoization     | 339 ms                                                      | 261 ms: 1.30x faster                                                       |
| deepcopy                   | 238 us                                                      | 187 us: 1.27x faster                                                       |
| async_tree_io              | 731 ms                                                      | 574 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 397 ms: 1.27x faster                                                       |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 389 ms: 1.26x faster                                                       |
| comprehensions             | 14.1 us                                                     | 12.0 us: 1.17x faster                                                      |
| deepcopy_memo              | 23.7 us                                                     | 20.9 us: 1.13x faster                                                      |
| deepcopy_reduce            | 2.09 us                                                     | 1.91 us: 1.09x faster                                                      |
| sqlite_synth               | 1.76 us                                                     | 1.62 us: 1.08x faster                                                      |
| bench_thread_pool          | 857 us                                                      | 802 us: 1.07x faster                                                       |
| regex_dna                  | 126 ms                                                      | 119 ms: 1.07x faster                                                       |
| go                         | 91.6 ms                                                     | 85.9 ms: 1.07x faster                                                      |
| generators                 | 22.5 ms                                                     | 21.2 ms: 1.06x faster                                                      |
| regex_effbot               | 1.62 ms                                                     | 1.57 ms: 1.03x faster                                                      |
| pathlib                    | 80.5 ms                                                     | 78.4 ms: 1.03x faster                                                      |
| pickle                     | 7.43 us                                                     | 7.27 us: 1.02x faster                                                      |
| dulwich_log                | 44.3 ms                                                     | 43.5 ms: 1.02x faster                                                      |
| float                      | 56.8 ms                                                     | 55.9 ms: 1.02x faster                                                      |
| sympy_sum                  | 91.5 ms                                                     | 90.1 ms: 1.02x faster                                                      |
| pidigits                   | 152 ms                                                      | 150 ms: 1.01x faster                                                       |
| coroutines                 | 14.3 ms                                                     | 14.1 ms: 1.01x faster                                                      |
| chaos                      | 43.3 ms                                                     | 43.6 ms: 1.01x slower                                                      |
| xml_etree_parse            | 93.0 ms                                                     | 94.0 ms: 1.01x slower                                                      |
| gc_traversal               | 1.52 ms                                                     | 1.54 ms: 1.01x slower                                                      |
| docutils                   | 1.66 sec                                                    | 1.68 sec: 1.01x slower                                                     |
| unpickle_list              | 2.75 us                                                     | 2.80 us: 1.02x slower                                                      |
| sympy_str                  | 175 ms                                                      | 179 ms: 1.02x slower                                                       |
| async_generators           | 239 ms                                                      | 244 ms: 1.02x slower                                                       |
| 2to3                       | 218 ms                                                      | 223 ms: 1.02x slower                                                       |
| sqlglot_normalize          | 187 ms                                                      | 192 ms: 1.03x slower                                                       |
| pickle_dict                | 18.4 us                                                     | 18.9 us: 1.03x slower                                                      |
| nqueens                    | 62.8 ms                                                     | 64.7 ms: 1.03x slower                                                      |
| tornado_http               | 89.5 ms                                                     | 92.2 ms: 1.03x slower                                                      |
| logging_silent             | 60.5 ns                                                     | 62.3 ns: 1.03x slower                                                      |
| sympy_integrate            | 13.0 ms                                                     | 13.4 ms: 1.03x slower                                                      |
| xml_etree_generate         | 55.8 ms                                                     | 57.6 ms: 1.03x slower                                                      |
| regex_v8                   | 14.2 ms                                                     | 14.7 ms: 1.03x slower                                                      |
| crypto_pyaes               | 48.5 ms                                                     | 50.2 ms: 1.03x slower                                                      |
| pycparser                  | 699 ms                                                      | 723 ms: 1.04x slower                                                       |
| meteor_contest             | 74.6 ms                                                     | 77.4 ms: 1.04x slower                                                      |
| pickle_list                | 2.83 us                                                     | 2.95 us: 1.04x slower                                                      |
| raytrace                   | 192 ms                                                      | 201 ms: 1.04x slower                                                       |
| regex_compile              | 87.5 ms                                                     | 91.4 ms: 1.04x slower                                                      |
| unpack_sequence            | 37.5 ns                                                     | 39.3 ns: 1.05x slower                                                      |
| sqlglot_optimize           | 34.5 ms                                                     | 36.3 ms: 1.05x slower                                                      |
| mdp                        | 1.37 sec                                                    | 1.44 sec: 1.05x slower                                                     |
| json_loads                 | 13.9 us                                                     | 14.7 us: 1.05x slower                                                      |
| deltablue                  | 2.16 ms                                                     | 2.28 ms: 1.06x slower                                                      |
| pprint_safe_repr           | 513 ms                                                      | 546 ms: 1.06x slower                                                       |
| spectral_norm              | 66.9 ms                                                     | 71.5 ms: 1.07x slower                                                      |
| pprint_pformat             | 1.05 sec                                                    | 1.12 sec: 1.08x slower                                                     |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.75 ms: 1.08x slower                                                      |
| sqlglot_transpile          | 1.02 ms                                                     | 1.10 ms: 1.08x slower                                                      |
| asyncio_tcp                | 487 ms                                                      | 526 ms: 1.08x slower                                                       |
| hexiom                     | 4.10 ms                                                     | 4.43 ms: 1.08x slower                                                      |
| scimark_lu                 | 58.9 ms                                                     | 63.7 ms: 1.08x slower                                                      |
| json_dumps                 | 5.70 ms                                                     | 6.19 ms: 1.09x slower                                                      |
| xml_etree_process          | 37.7 ms                                                     | 41.0 ms: 1.09x slower                                                      |
| pickle_pure_python         | 195 us                                                      | 213 us: 1.09x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                     | 17.7 ms: 1.09x slower                                                      |
| sympy_expand               | 284 ms                                                      | 310 ms: 1.09x slower                                                       |
| django_template            | 22.9 ms                                                     | 25.1 ms: 1.09x slower                                                      |
| sqlglot_parse              | 804 us                                                      | 885 us: 1.10x slower                                                       |
| unpickle                   | 8.18 us                                                     | 9.04 us: 1.10x slower                                                      |
| unpickle_pure_python       | 133 us                                                      | 148 us: 1.11x slower                                                       |
| pyflate                    | 295 ms                                                      | 328 ms: 1.11x slower                                                       |
| python_startup             | 19.5 ms                                                     | 21.9 ms: 1.13x slower                                                      |
| coverage                   | 40.8 ms                                                     | 46.0 ms: 1.13x slower                                                      |
| richards                   | 28.4 ms                                                     | 32.0 ms: 1.13x slower                                                      |
| richards_super             | 32.1 ms                                                     | 36.2 ms: 1.13x slower                                                      |
| scimark_fft                | 184 ms                                                      | 209 ms: 1.13x slower                                                       |
| scimark_monte_carlo        | 43.7 ms                                                     | 49.5 ms: 1.13x slower                                                      |
| nbody                      | 71.9 ms                                                     | 82.0 ms: 1.14x slower                                                      |
| typing_runtime_protocols   | 95.1 us                                                     | 110 us: 1.16x slower                                                       |
| scimark_sor                | 78.8 ms                                                     | 91.3 ms: 1.16x slower                                                      |
| tomli_loads                | 1.37 sec                                                    | 1.59 sec: 1.16x slower                                                     |
| create_gc_cycles           | 752 us                                                      | 890 us: 1.18x slower                                                       |
| telco                      | 4.13 ms                                                     | 4.89 ms: 1.19x slower                                                      |
| fannkuch                   | 247 ms                                                      | 305 ms: 1.24x slower                                                       |
| json                       | 3.05 ms                                                     | 4.33 ms: 1.42x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (5): mako, xml_etree_iterparse, bench_mp_pool, logging_format, logging_simple
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-pythonperf1-amd64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.68% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown