# Results vs. 3.12.0

- fork: faster-cpython
- ref: load_int
- machine: linux-x86_64
- commit hash: 1b5b50f
- commit date: 2024-10-24
- overall geometric mean: 1.071x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                 |
| docutils       | 2.77 sec                                               | 2.67 sec: 1.04x faster                                               |
| tornado_http   | 103 ms                                                 | 90.1 ms: 1.14x faster                                                |
| Geometric mean | (ref)                                                  | 1.09x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 384 ms: 1.50x faster                                                 |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 413 ms: 1.40x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 322 ms: 1.39x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 838 ms: 1.38x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 564 ms: 1.29x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 574 ms: 1.26x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 982 ms: 1.20x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.35x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 79.3 ms: 1.07x faster                                                |
| nbody          | 97.0 ms                                                | 96.0 ms: 1.01x faster                                                |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 129 ms: 1.15x faster                                                 |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                 |
| regex_v8       | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.08 sec: 1.12x faster                                               |
| json_loads           | 28.5 us                                                | 26.1 us: 1.09x faster                                                |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 311 us: 1.04x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 86.1 ms: 1.04x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 158 ms: 1.01x faster                                                 |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                         |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                |
| python_startup         | 9.55 ms                                                | 11.7 ms: 1.23x slower                                                |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.5 ms: 1.03x faster                                                |
| django_template | 34.6 ms                                                | 34.8 ms: 1.01x slower                                                |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 384 ms: 1.50x faster                                                 |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                                 |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 413 ms: 1.40x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 322 ms: 1.39x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 838 ms: 1.38x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 30.8 us: 1.32x faster                                                |
| comprehensions             | 21.8 us                                                | 16.9 us: 1.29x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 564 ms: 1.29x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 574 ms: 1.26x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 982 ms: 1.20x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.20x faster                                                |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                                |
| go                         | 139 ms                                                 | 121 ms: 1.16x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.59 us: 1.15x faster                                                |
| regex_compile              | 148 ms                                                 | 129 ms: 1.15x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                 |
| sqlalchemy_declarative     | 147 ms                                                 | 128 ms: 1.15x faster                                                 |
| raytrace                   | 312 ms                                                 | 273 ms: 1.14x faster                                                 |
| tornado_http               | 103 ms                                                 | 90.1 ms: 1.14x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.30 ms: 1.13x faster                                                |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.08 sec: 1.12x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 73.6 ms: 1.11x faster                                                |
| generators                 | 31.2 ms                                                | 28.3 ms: 1.10x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.0 ms: 1.10x faster                                                |
| chaos                      | 67.0 ms                                                | 60.8 ms: 1.10x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 68.4 ms: 1.10x faster                                                |
| json_loads                 | 28.5 us                                                | 26.1 us: 1.09x faster                                                |
| json                       | 5.26 ms                                                | 4.83 ms: 1.09x faster                                                |
| pyflate                    | 482 ms                                                 | 446 ms: 1.08x faster                                                 |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.08x faster                                                |
| dulwich_log                | 68.5 ms                                                | 63.9 ms: 1.07x faster                                                |
| async_generators           | 463 ms                                                 | 433 ms: 1.07x faster                                                 |
| float                      | 84.7 ms                                                | 79.3 ms: 1.07x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                                 |
| scimark_fft                | 382 ms                                                 | 358 ms: 1.07x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 728 ms: 1.07x faster                                                 |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                |
| sympy_expand               | 478 ms                                                 | 455 ms: 1.05x faster                                                 |
| mdp                        | 2.63 sec                                               | 2.51 sec: 1.05x faster                                               |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.05x faster                                               |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.05x faster                                                 |
| nqueens                    | 83.3 ms                                                | 79.7 ms: 1.05x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.84 ms: 1.04x faster                                                |
| pickle_pure_python         | 324 us                                                 | 311 us: 1.04x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.67 sec: 1.04x faster                                               |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 86.1 ms: 1.04x faster                                                |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                 |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.03x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 59.9 ms: 1.03x faster                                                |
| sqlglot_optimize           | 54.8 ms                                                | 53.3 ms: 1.03x faster                                                |
| fannkuch                   | 417 ms                                                 | 406 ms: 1.03x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.29 ms: 1.02x faster                                                |
| logging_silent             | 104 ns                                                 | 103 ns: 1.02x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 158 ms: 1.01x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.17 sec: 1.01x faster                                               |
| nbody                      | 97.0 ms                                                | 96.0 ms: 1.01x faster                                                |
| bench_thread_pool          | 842 us                                                 | 837 us: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x slower                                                 |
| django_template            | 34.6 ms                                                | 34.8 ms: 1.01x slower                                                |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.01x slower                                                 |
| coroutines                 | 23.2 ms                                                | 23.6 ms: 1.02x slower                                                |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                 |
| richards_super             | 51.5 ms                                                | 52.7 ms: 1.02x slower                                                |
| richards                   | 45.8 ms                                                | 46.9 ms: 1.02x slower                                                |
| regex_v8                   | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                |
| telco                      | 7.10 ms                                                | 8.04 ms: 1.13x slower                                                |
| coverage                   | 72.7 ms                                                | 83.6 ms: 1.15x slower                                                |
| python_startup             | 9.55 ms                                                | 11.7 ms: 1.23x slower                                                |
| gc_traversal               | 3.79 ms                                                | 4.70 ms: 1.24x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 2.66 ms: 1.80x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 77.8 ms: 3.24x slower                                                |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                         |

Benchmark hidden because not significant (3): xml_etree_iterparse, regex_effbot, spectral_norm
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20241024-3.14.0a1+-1b5b50f/bm-20241024-linux-x86_64-faster%2dcpython-load_int-3.14.0a1+-1b5b50f.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.071x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.08x