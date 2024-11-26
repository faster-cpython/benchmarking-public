# Results vs. 3.12.0

- fork: brandtbucher
- ref: warmup_65536
- machine: linux-x86_64
- commit hash: c17f578
- commit date: 2024-11-12
- overall geometric mean: 1.066x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                                 |
| docutils       | 2.77 sec                                               | 2.81 sec: 1.01x slower                                               |
| Geometric mean | (ref)                                                  | 1.02x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 378 ms: 1.52x faster                                                 |
| async_tree_none            | 472 ms                                                 | 332 ms: 1.42x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 323 ms: 1.39x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 417 ms: 1.38x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 868 ms: 1.33x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 564 ms: 1.29x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 580 ms: 1.25x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 979 ms: 1.21x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.35x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 82.5 ms: 1.18x faster                                                |
| float          | 84.7 ms                                                | 77.1 ms: 1.10x faster                                                |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                 |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                 |
| regex_effbot   | 3.61 ms                                                | 3.74 ms: 1.04x slower                                                |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.98 sec: 1.18x faster                                               |
| unpickle_pure_python | 230 us                                                 | 200 us: 1.15x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 78.7 ms: 1.13x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 55.2 ms: 1.12x faster                                                |
| json_loads           | 28.5 us                                                | 27.1 us: 1.05x faster                                                |
| xml_etree_iterparse  | 107 ms                                                 | 103 ms: 1.03x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 318 us: 1.02x faster                                                 |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.06x slower                                                |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                         |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                |
| django_template | 34.6 ms                                                | 36.1 ms: 1.04x slower                                                |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 378 ms: 1.52x faster                                                 |
| async_tree_none            | 472 ms                                                 | 332 ms: 1.42x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 323 ms: 1.39x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 29.4 us: 1.38x faster                                                |
| async_tree_memoization     | 578 ms                                                 | 417 ms: 1.38x faster                                                 |
| deepcopy                   | 371 us                                                 | 272 us: 1.37x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 868 ms: 1.33x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 564 ms: 1.29x faster                                                 |
| comprehensions             | 21.8 us                                                | 17.4 us: 1.25x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 580 ms: 1.25x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.75 us: 1.22x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 979 ms: 1.21x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 69.0 ms: 1.19x faster                                                |
| tomli_loads                | 2.33 sec                                               | 1.98 sec: 1.18x faster                                               |
| nbody                      | 97.0 ms                                                | 82.5 ms: 1.18x faster                                                |
| scimark_fft                | 382 ms                                                 | 326 ms: 1.17x faster                                                 |
| mako                       | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.19 ms: 1.16x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 65.2 ms: 1.15x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 200 us: 1.15x faster                                                 |
| logging_format             | 7.23 us                                                | 6.30 us: 1.15x faster                                                |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                 |
| raytrace                   | 312 ms                                                 | 273 ms: 1.14x faster                                                 |
| sqlalchemy_declarative     | 147 ms                                                 | 129 ms: 1.14x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 78.7 ms: 1.13x faster                                                |
| logging_simple             | 6.46 us                                                | 5.72 us: 1.13x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 55.2 ms: 1.12x faster                                                |
| chaos                      | 67.0 ms                                                | 60.0 ms: 1.12x faster                                                |
| float                      | 84.7 ms                                                | 77.1 ms: 1.10x faster                                                |
| go                         | 139 ms                                                 | 127 ms: 1.09x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.63 ms: 1.09x faster                                                |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                                 |
| sympy_str                  | 300 ms                                                 | 275 ms: 1.09x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 715 ms: 1.09x faster                                                 |
| fannkuch                   | 417 ms                                                 | 385 ms: 1.08x faster                                                 |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.07x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                               |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.5 ms: 1.07x faster                                                |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                |
| logging_silent             | 104 ns                                                 | 98.7 ns: 1.06x faster                                                |
| json                       | 5.26 ms                                                | 4.97 ms: 1.06x faster                                                |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                |
| json_loads                 | 28.5 us                                                | 27.1 us: 1.05x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 20.4 ms: 1.05x faster                                                |
| dulwich_log                | 68.5 ms                                                | 65.7 ms: 1.04x faster                                                |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.04x faster                                                 |
| pyflate                    | 482 ms                                                 | 464 ms: 1.04x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 103 ms: 1.03x faster                                                 |
| mdp                        | 2.63 sec                                               | 2.55 sec: 1.03x faster                                               |
| sympy_expand               | 478 ms                                                 | 467 ms: 1.02x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 318 us: 1.02x faster                                                 |
| meteor_contest             | 112 ms                                                 | 111 ms: 1.02x faster                                                 |
| richards                   | 45.8 ms                                                | 45.2 ms: 1.01x faster                                                |
| sqlglot_optimize           | 54.8 ms                                                | 54.2 ms: 1.01x faster                                                |
| sqlite_synth               | 2.83 us                                                | 2.81 us: 1.01x faster                                                |
| sqlglot_normalize          | 110 ms                                                 | 110 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                 |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                 |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                                |
| pycparser                  | 1.18 sec                                               | 1.19 sec: 1.01x slower                                               |
| docutils                   | 2.77 sec                                               | 2.81 sec: 1.01x slower                                               |
| richards_super             | 51.5 ms                                                | 52.4 ms: 1.02x slower                                                |
| python_startup_no_site     | 6.94 ms                                                | 7.09 ms: 1.02x slower                                                |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                 |
| bench_thread_pool          | 842 us                                                 | 869 us: 1.03x slower                                                 |
| regex_effbot               | 3.61 ms                                                | 3.74 ms: 1.04x slower                                                |
| spectral_norm              | 115 ms                                                 | 120 ms: 1.04x slower                                                 |
| django_template            | 34.6 ms                                                | 36.1 ms: 1.04x slower                                                |
| hexiom                     | 6.41 ms                                                | 6.71 ms: 1.05x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.06x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.06x slower                                                |
| nqueens                    | 83.3 ms                                                | 90.5 ms: 1.09x slower                                                |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.09x slower                                                |
| telco                      | 7.10 ms                                                | 7.80 ms: 1.10x slower                                                |
| coverage                   | 72.7 ms                                                | 84.1 ms: 1.16x slower                                                |
| generators                 | 31.2 ms                                                | 36.4 ms: 1.16x slower                                                |
| gc_traversal               | 3.79 ms                                                | 4.80 ms: 1.27x slower                                                |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 2.70 ms: 1.83x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 79.2 ms: 3.30x slower                                                |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                         |

Benchmark hidden because not significant (2): async_generators, xml_etree_parse
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241112-3.14.0a1+-c17f578-JIT/bm-20241112-linux-x86_64-brandtbucher-warmup_65536-3.14.0a1+-c17f578.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.066x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.10x