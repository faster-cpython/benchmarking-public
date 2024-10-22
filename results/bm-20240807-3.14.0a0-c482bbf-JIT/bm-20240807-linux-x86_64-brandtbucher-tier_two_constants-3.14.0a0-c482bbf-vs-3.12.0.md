# Results vs. 3.12.0

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: c482bbf
- commit date: 2024-08-07
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.77 sec                                               | 2.91 sec: 1.05x slower                                                    |
| tornado_http   | 103 ms                                                 | 92.7 ms: 1.11x faster                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 392 ms: 1.47x faster                                                      |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.46x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 420 ms: 1.38x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 863 ms: 1.37x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 533 ms: 1.36x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 901 ms: 1.28x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.38x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 78.1 ms: 1.24x faster                                                     |
| float          | 84.7 ms                                                | 70.0 ms: 1.21x faster                                                     |
| pidigits       | 187 ms                                                 | 185 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                  | 1.15x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.10x faster                                                      |
| regex_effbot   | 3.61 ms                                                | 3.84 ms: 1.06x slower                                                     |
| regex_dna      | 212 ms                                                 | 228 ms: 1.07x slower                                                      |
| regex_v8       | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                    |
| xml_etree_generate   | 89.2 ms                                                | 79.4 ms: 1.12x faster                                                     |
| xml_etree_process    | 61.7 ms                                                | 55.8 ms: 1.11x faster                                                     |
| pickle_pure_python   | 324 us                                                 | 295 us: 1.10x faster                                                      |
| xml_etree_parse      | 159 ms                                                 | 146 ms: 1.09x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 99.2 ms: 1.08x faster                                                     |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.06x faster                                                      |
| json_loads           | 28.5 us                                                | 28.0 us: 1.02x faster                                                     |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                     |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.20 ms: 1.04x slower                                                     |
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.70 ms: 1.23x faster                                                     |
| django_template | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 300 ms: 1.50x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 392 ms: 1.47x faster                                                      |
| async_tree_none            | 472 ms                                                 | 324 ms: 1.46x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 28.6 us: 1.43x faster                                                     |
| async_tree_memoization     | 578 ms                                                 | 420 ms: 1.38x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 863 ms: 1.37x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 533 ms: 1.36x faster                                                      |
| deepcopy                   | 371 us                                                 | 274 us: 1.35x faster                                                      |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                     |
| async_tree_io              | 1.16 sec                                               | 901 ms: 1.28x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 567 ms: 1.28x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 60.1 ms: 1.25x faster                                                     |
| scimark_fft                | 382 ms                                                 | 306 ms: 1.25x faster                                                      |
| nbody                      | 97.0 ms                                                | 78.1 ms: 1.24x faster                                                     |
| mako                       | 11.9 ms                                                | 9.70 ms: 1.23x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 66.9 ms: 1.22x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.92 sec: 1.21x faster                                                    |
| float                      | 84.7 ms                                                | 70.0 ms: 1.21x faster                                                     |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                     |
| raytrace                   | 312 ms                                                 | 263 ms: 1.19x faster                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.31 ms: 1.17x faster                                                     |
| logging_format             | 7.23 us                                                | 6.18 us: 1.17x faster                                                     |
| fannkuch                   | 417 ms                                                 | 361 ms: 1.16x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.61 us: 1.15x faster                                                     |
| chaos                      | 67.0 ms                                                | 58.2 ms: 1.15x faster                                                     |
| pyflate                    | 482 ms                                                 | 421 ms: 1.15x faster                                                      |
| xml_etree_generate         | 89.2 ms                                                | 79.4 ms: 1.12x faster                                                     |
| richards                   | 45.8 ms                                                | 41.1 ms: 1.12x faster                                                     |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                      |
| tornado_http               | 103 ms                                                 | 92.7 ms: 1.11x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 55.8 ms: 1.11x faster                                                     |
| regex_compile              | 148 ms                                                 | 134 ms: 1.10x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 295 us: 1.10x faster                                                      |
| richards_super             | 51.5 ms                                                | 47.0 ms: 1.10x faster                                                     |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                                      |
| xml_etree_parse            | 159 ms                                                 | 146 ms: 1.09x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 720 ms: 1.08x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 99.2 ms: 1.08x faster                                                     |
| deltablue                  | 3.72 ms                                                | 3.48 ms: 1.07x faster                                                     |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.06x faster                                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                     |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.05x faster                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.04x faster                                                    |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                     |
| logging_silent             | 104 ns                                                 | 102 ns: 1.03x faster                                                      |
| bench_thread_pool          | 842 us                                                 | 819 us: 1.03x faster                                                      |
| mdp                        | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                    |
| json                       | 5.26 ms                                                | 5.16 ms: 1.02x faster                                                     |
| json_loads                 | 28.5 us                                                | 28.0 us: 1.02x faster                                                     |
| coroutines                 | 23.2 ms                                                | 22.8 ms: 1.02x faster                                                     |
| pidigits                   | 187 ms                                                 | 185 ms: 1.01x faster                                                      |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                     |
| async_generators           | 463 ms                                                 | 459 ms: 1.01x faster                                                      |
| gc_traversal               | 3.79 ms                                                | 3.77 ms: 1.01x faster                                                     |
| sympy_sum                  | 169 ms                                                 | 170 ms: 1.00x slower                                                      |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                    |
| sqlglot_normalize          | 110 ms                                                 | 112 ms: 1.02x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 55.7 ms: 1.02x slower                                                     |
| nqueens                    | 83.3 ms                                                | 84.8 ms: 1.02x slower                                                     |
| asyncio_tcp                | 491 ms                                                 | 500 ms: 1.02x slower                                                      |
| go                         | 139 ms                                                 | 143 ms: 1.03x slower                                                      |
| hexiom                     | 6.41 ms                                                | 6.64 ms: 1.04x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 7.20 ms: 1.04x slower                                                     |
| django_template            | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                     |
| sympy_integrate            | 21.4 ms                                                | 22.5 ms: 1.05x slower                                                     |
| docutils                   | 2.77 sec                                               | 2.91 sec: 1.05x slower                                                    |
| generators                 | 31.2 ms                                                | 33.1 ms: 1.06x slower                                                     |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                      |
| sympy_expand               | 478 ms                                                 | 508 ms: 1.06x slower                                                      |
| regex_effbot               | 3.61 ms                                                | 3.84 ms: 1.06x slower                                                     |
| regex_dna                  | 212 ms                                                 | 228 ms: 1.07x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 25.4 ms: 1.10x slower                                                     |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                     |
| telco                      | 7.10 ms                                                | 7.90 ms: 1.11x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.77 ms: 1.20x slower                                                     |
| coverage                   | 72.7 ms                                                | 90.9 ms: 1.25x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                              |

Benchmark hidden because not significant (4): sympy_str, bench_mp_pool, 2to3, pycparser
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240807-3.14.0a0-c482bbf-JIT/bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.04x