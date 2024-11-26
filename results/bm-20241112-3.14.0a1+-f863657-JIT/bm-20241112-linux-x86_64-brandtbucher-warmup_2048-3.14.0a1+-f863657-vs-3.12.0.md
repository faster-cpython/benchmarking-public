# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmup_2048
- machine: linux-x86_64
- commit hash: f863657
- commit date: 2024-11-12
- overall geometric mean: 1.062x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 267 ms: 1.03x faster                                                |
| docutils       | 2.77 sec                                               | 2.91 sec: 1.05x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 380 ms: 1.51x faster                                                |
| async_tree_none            | 472 ms                                                 | 333 ms: 1.42x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 319 ms: 1.41x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 415 ms: 1.39x faster                                                |
| async_tree_io              | 1.16 sec                                               | 862 ms: 1.34x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 559 ms: 1.30x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 576 ms: 1.26x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 964 ms: 1.23x faster                                                |
| Geometric mean             | (ref)                                                  | 1.35x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 81.9 ms: 1.18x faster                                               |
| float          | 84.7 ms                                                | 76.0 ms: 1.11x faster                                               |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                  | 1.10x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 135 ms: 1.10x faster                                                |
| regex_dna      | 212 ms                                                 | 218 ms: 1.03x slower                                                |
| regex_effbot   | 3.61 ms                                                | 3.72 ms: 1.03x slower                                               |
| regex_v8       | 23.1 ms                                                | 24.7 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.97 sec: 1.18x faster                                              |
| xml_etree_generate   | 89.2 ms                                                | 79.3 ms: 1.12x faster                                               |
| xml_etree_process    | 61.7 ms                                                | 56.2 ms: 1.10x faster                                               |
| json_loads           | 28.5 us                                                | 27.0 us: 1.06x faster                                               |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.05x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 103 ms: 1.04x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 154 ms: 1.03x faster                                                |
| json_dumps           | 10.4 ms                                                | 10.9 ms: 1.05x slower                                               |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                        |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.05 ms: 1.02x slower                                               |
| python_startup         | 9.55 ms                                                | 12.7 ms: 1.33x slower                                               |
| Geometric mean         | (ref)                                                  | 1.16x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.2 ms: 1.17x faster                                               |
| django_template | 34.6 ms                                                | 36.4 ms: 1.05x slower                                               |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 380 ms: 1.51x faster                                                |
| async_tree_none            | 472 ms                                                 | 333 ms: 1.42x faster                                                |
| async_tree_none_tg         | 450 ms                                                 | 319 ms: 1.41x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 415 ms: 1.39x faster                                                |
| deepcopy_memo              | 40.7 us                                                | 29.4 us: 1.39x faster                                               |
| deepcopy                   | 371 us                                                 | 270 us: 1.37x faster                                                |
| async_tree_io              | 1.16 sec                                               | 862 ms: 1.34x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 559 ms: 1.30x faster                                                |
| comprehensions             | 21.8 us                                                | 17.2 us: 1.26x faster                                               |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 576 ms: 1.26x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 964 ms: 1.23x faster                                                |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                               |
| crypto_pyaes               | 81.9 ms                                                | 68.3 ms: 1.20x faster                                               |
| scimark_fft                | 382 ms                                                 | 319 ms: 1.20x faster                                                |
| nbody                      | 97.0 ms                                                | 81.9 ms: 1.18x faster                                               |
| tomli_loads                | 2.33 sec                                               | 1.97 sec: 1.18x faster                                              |
| logging_format             | 7.23 us                                                | 6.14 us: 1.18x faster                                               |
| mako                       | 11.9 ms                                                | 10.2 ms: 1.17x faster                                               |
| scimark_monte_carlo        | 75.1 ms                                                | 65.1 ms: 1.15x faster                                               |
| logging_simple             | 6.46 us                                                | 5.61 us: 1.15x faster                                               |
| richards                   | 45.8 ms                                                | 39.9 ms: 1.15x faster                                               |
| raytrace                   | 312 ms                                                 | 277 ms: 1.13x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.29 ms: 1.13x faster                                               |
| richards_super             | 51.5 ms                                                | 45.7 ms: 1.13x faster                                               |
| xml_etree_generate         | 89.2 ms                                                | 79.3 ms: 1.12x faster                                               |
| float                      | 84.7 ms                                                | 76.0 ms: 1.11x faster                                               |
| chaos                      | 67.0 ms                                                | 60.5 ms: 1.11x faster                                               |
| xml_etree_process          | 61.7 ms                                                | 56.2 ms: 1.10x faster                                               |
| regex_compile              | 148 ms                                                 | 135 ms: 1.10x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.62 ms: 1.09x faster                                               |
| sqlalchemy_declarative     | 147 ms                                                 | 136 ms: 1.08x faster                                                |
| fannkuch                   | 417 ms                                                 | 387 ms: 1.08x faster                                                |
| json                       | 5.26 ms                                                | 4.91 ms: 1.07x faster                                               |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                                |
| logging_silent             | 104 ns                                                 | 97.9 ns: 1.07x faster                                               |
| pprint_safe_repr           | 776 ms                                                 | 733 ms: 1.06x faster                                                |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                |
| json_loads                 | 28.5 us                                                | 27.0 us: 1.06x faster                                               |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.7 ms: 1.06x faster                                               |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.05x faster                                                |
| pyflate                    | 482 ms                                                 | 459 ms: 1.05x faster                                                |
| go                         | 139 ms                                                 | 134 ms: 1.04x faster                                                |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                              |
| xml_etree_iterparse        | 107 ms                                                 | 103 ms: 1.04x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 154 ms: 1.03x faster                                                |
| 2to3                       | 274 ms                                                 | 267 ms: 1.03x faster                                                |
| async_generators           | 463 ms                                                 | 452 ms: 1.02x faster                                                |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                              |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.02x faster                                               |
| sqlglot_transpile          | 1.68 ms                                                | 1.65 ms: 1.02x faster                                               |
| dulwich_log                | 68.5 ms                                                | 67.4 ms: 1.02x faster                                               |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                               |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                                |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.01x slower                                               |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.01x slower                                                |
| python_startup_no_site     | 6.94 ms                                                | 7.05 ms: 1.02x slower                                               |
| sympy_integrate            | 21.4 ms                                                | 21.9 ms: 1.02x slower                                               |
| regex_dna                  | 212 ms                                                 | 218 ms: 1.03x slower                                                |
| sqlglot_optimize           | 54.8 ms                                                | 56.4 ms: 1.03x slower                                               |
| regex_effbot               | 3.61 ms                                                | 3.72 ms: 1.03x slower                                               |
| mdp                        | 2.63 sec                                               | 2.73 sec: 1.04x slower                                              |
| bench_thread_pool          | 842 us                                                 | 877 us: 1.04x slower                                                |
| docutils                   | 2.77 sec                                               | 2.91 sec: 1.05x slower                                              |
| django_template            | 34.6 ms                                                | 36.4 ms: 1.05x slower                                               |
| nqueens                    | 83.3 ms                                                | 87.7 ms: 1.05x slower                                               |
| json_dumps                 | 10.4 ms                                                | 10.9 ms: 1.05x slower                                               |
| sympy_expand               | 478 ms                                                 | 504 ms: 1.05x slower                                                |
| regex_v8                   | 23.1 ms                                                | 24.7 ms: 1.07x slower                                               |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                |
| telco                      | 7.10 ms                                                | 7.63 ms: 1.07x slower                                               |
| hexiom                     | 6.41 ms                                                | 7.13 ms: 1.11x slower                                               |
| generators                 | 31.2 ms                                                | 35.8 ms: 1.15x slower                                               |
| coverage                   | 72.7 ms                                                | 85.1 ms: 1.17x slower                                               |
| gc_traversal               | 3.79 ms                                                | 4.52 ms: 1.19x slower                                               |
| python_startup             | 9.55 ms                                                | 12.7 ms: 1.33x slower                                               |
| create_gc_cycles           | 1.48 ms                                                | 2.67 ms: 1.81x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 78.8 ms: 3.28x slower                                               |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                        |

Benchmark hidden because not significant (4): sympy_sum, spectral_norm, sympy_str, pickle_pure_python
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241112-3.14.0a1+-f863657-JIT/bm-20241112-linux-x86_64-brandtbucher-warmup_2048-3.14.0a1+-f863657.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.062x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.11x