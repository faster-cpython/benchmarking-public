# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: c482bbf
- commit date: 2024-08-07
- overall geometric mean: 1.05x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.83 sec                                                   | 2.91 sec: 1.03x slower                                                    |
| html5lib       | 67.2 ms                                                    | 66.1 ms: 1.02x faster                                                     |
| tornado_http   | 94.6 ms                                                    | 92.7 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                      | 1.00x faster                                                              |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 378 ms                                                     | 324 ms: 1.17x faster                                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 392 ms: 1.13x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 420 ms: 1.10x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 533 ms: 1.10x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 863 ms: 1.09x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 567 ms: 1.08x faster                                                      |
| async_tree_io              | 939 ms                                                     | 901 ms: 1.04x faster                                                      |
| Geometric mean             | (ref)                                                      | 1.10x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 78.1 ms: 1.13x faster                                                     |
| float          | 78.9 ms                                                    | 70.0 ms: 1.13x faster                                                     |
| pidigits       | 191 ms                                                     | 185 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                      | 1.10x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 137 ms                                                     | 134 ms: 1.02x faster                                                      |
| regex_v8       | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                                     |
| regex_dna      | 221 ms                                                     | 228 ms: 1.03x slower                                                      |
| regex_effbot   | 3.67 ms                                                    | 3.84 ms: 1.05x slower                                                     |
| Geometric mean | (ref)                                                      | 1.02x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|---------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse     | 162 ms                                                     | 146 ms: 1.11x faster                                                      |
| tomli_loads         | 2.12 sec                                                   | 1.92 sec: 1.10x faster                                                    |
| xml_etree_generate  | 87.4 ms                                                    | 79.4 ms: 1.10x faster                                                     |
| xml_etree_process   | 61.2 ms                                                    | 55.8 ms: 1.10x faster                                                     |
| xml_etree_iterparse | 107 ms                                                     | 99.2 ms: 1.08x faster                                                     |
| json_dumps          | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                     |
| pickle_pure_python  | 305 us                                                     | 295 us: 1.03x faster                                                      |
| json_loads          | 28.9 us                                                    | 28.0 us: 1.03x faster                                                     |
| Geometric mean      | (ref)                                                      | 1.07x faster                                                              |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                     |
| python_startup_no_site | 7.11 ms                                                    | 7.20 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.70 ms: 1.16x faster                                                     |
| genshi_text     | 23.7 ms                                                    | 24.0 ms: 1.01x slower                                                     |
| genshi_xml      | 51.6 ms                                                    | 53.4 ms: 1.03x slower                                                     |
| django_template | 34.8 ms                                                    | 36.0 ms: 1.03x slower                                                     |
| Geometric mean  | (ref)                                                      | 1.02x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240807-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c482bbf |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 28.6 us: 1.39x faster                                                     |
| deepcopy                   | 367 us                                                     | 274 us: 1.34x faster                                                      |
| scimark_fft                | 392 ms                                                     | 306 ms: 1.28x faster                                                      |
| richards                   | 50.9 ms                                                    | 41.1 ms: 1.24x faster                                                     |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.31 ms: 1.22x faster                                                     |
| richards_super             | 57.4 ms                                                    | 47.0 ms: 1.22x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                    | 2.74 us: 1.22x faster                                                     |
| async_tree_none            | 378 ms                                                     | 324 ms: 1.17x faster                                                      |
| mako                       | 11.2 ms                                                    | 9.70 ms: 1.16x faster                                                     |
| crypto_pyaes               | 77.5 ms                                                    | 66.9 ms: 1.16x faster                                                     |
| scimark_monte_carlo        | 69.2 ms                                                    | 60.1 ms: 1.15x faster                                                     |
| pyflate                    | 484 ms                                                     | 421 ms: 1.15x faster                                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 392 ms: 1.13x faster                                                      |
| nbody                      | 88.3 ms                                                    | 78.1 ms: 1.13x faster                                                     |
| spectral_norm              | 116 ms                                                     | 103 ms: 1.13x faster                                                      |
| float                      | 78.9 ms                                                    | 70.0 ms: 1.13x faster                                                     |
| bpe_tokeniser              | 5.02 sec                                                   | 4.47 sec: 1.12x faster                                                    |
| async_tree_none_tg         | 336 ms                                                     | 300 ms: 1.12x faster                                                      |
| fannkuch                   | 402 ms                                                     | 361 ms: 1.11x faster                                                      |
| xml_etree_parse            | 162 ms                                                     | 146 ms: 1.11x faster                                                      |
| tomli_loads                | 2.12 sec                                                   | 1.92 sec: 1.10x faster                                                    |
| async_tree_memoization     | 463 ms                                                     | 420 ms: 1.10x faster                                                      |
| xml_etree_generate         | 87.4 ms                                                    | 79.4 ms: 1.10x faster                                                     |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 533 ms: 1.10x faster                                                      |
| xml_etree_process          | 61.2 ms                                                    | 55.8 ms: 1.10x faster                                                     |
| async_tree_io_tg           | 936 ms                                                     | 863 ms: 1.09x faster                                                      |
| mdp                        | 2.79 sec                                                   | 2.57 sec: 1.08x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                     | 99.2 ms: 1.08x faster                                                     |
| scimark_lu                 | 122 ms                                                     | 112 ms: 1.08x faster                                                      |
| scimark_sor                | 127 ms                                                     | 118 ms: 1.08x faster                                                      |
| pathlib                    | 17.3 ms                                                    | 16.1 ms: 1.08x faster                                                     |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 567 ms: 1.08x faster                                                      |
| telco                      | 8.41 ms                                                    | 7.90 ms: 1.07x faster                                                     |
| gc_traversal               | 3.98 ms                                                    | 3.77 ms: 1.06x faster                                                     |
| chaos                      | 61.3 ms                                                    | 58.2 ms: 1.05x faster                                                     |
| pprint_safe_repr           | 758 ms                                                     | 720 ms: 1.05x faster                                                      |
| logging_format             | 6.47 us                                                    | 6.18 us: 1.05x faster                                                     |
| async_tree_io              | 939 ms                                                     | 901 ms: 1.04x faster                                                      |
| json_dumps                 | 10.7 ms                                                    | 10.3 ms: 1.04x faster                                                     |
| meteor_contest             | 110 ms                                                     | 106 ms: 1.04x faster                                                      |
| pickle_pure_python         | 305 us                                                     | 295 us: 1.03x faster                                                      |
| pprint_pformat             | 1.56 sec                                                   | 1.50 sec: 1.03x faster                                                    |
| pidigits                   | 191 ms                                                     | 185 ms: 1.03x faster                                                      |
| thrift                     | 823 us                                                     | 798 us: 1.03x faster                                                      |
| json_loads                 | 28.9 us                                                    | 28.0 us: 1.03x faster                                                     |
| logging_silent             | 105 ns                                                     | 102 ns: 1.03x faster                                                      |
| json                       | 5.31 ms                                                    | 5.16 ms: 1.03x faster                                                     |
| create_gc_cycles           | 1.82 ms                                                    | 1.77 ms: 1.02x faster                                                     |
| logging_simple             | 5.74 us                                                    | 5.61 us: 1.02x faster                                                     |
| coverage                   | 93.1 ms                                                    | 90.9 ms: 1.02x faster                                                     |
| sqlglot_parse              | 1.32 ms                                                    | 1.29 ms: 1.02x faster                                                     |
| tornado_http               | 94.6 ms                                                    | 92.7 ms: 1.02x faster                                                     |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                      |
| regex_compile              | 137 ms                                                     | 134 ms: 1.02x faster                                                      |
| bench_thread_pool          | 834 us                                                     | 819 us: 1.02x faster                                                      |
| html5lib                   | 67.2 ms                                                    | 66.1 ms: 1.02x faster                                                     |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.81 sec: 1.02x faster                                                    |
| coroutines                 | 23.2 ms                                                    | 22.8 ms: 1.02x faster                                                     |
| asyncio_tcp                | 508 ms                                                     | 500 ms: 1.02x faster                                                      |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.01x faster                                                     |
| raytrace                   | 267 ms                                                     | 263 ms: 1.01x faster                                                      |
| go                         | 145 ms                                                     | 143 ms: 1.01x faster                                                      |
| sqlglot_transpile          | 1.63 ms                                                    | 1.62 ms: 1.01x faster                                                     |
| comprehensions             | 16.6 us                                                    | 16.5 us: 1.01x faster                                                     |
| sqlglot_optimize           | 55.5 ms                                                    | 55.7 ms: 1.00x slower                                                     |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                     |
| regex_v8                   | 25.1 ms                                                    | 25.4 ms: 1.01x slower                                                     |
| python_startup_no_site     | 7.11 ms                                                    | 7.20 ms: 1.01x slower                                                     |
| genshi_text                | 23.7 ms                                                    | 24.0 ms: 1.01x slower                                                     |
| typing_runtime_protocols   | 165 us                                                     | 167 us: 1.02x slower                                                      |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                                      |
| pycparser                  | 1.16 sec                                                   | 1.19 sec: 1.02x slower                                                    |
| docutils                   | 2.83 sec                                                   | 2.91 sec: 1.03x slower                                                    |
| regex_dna                  | 221 ms                                                     | 228 ms: 1.03x slower                                                      |
| genshi_xml                 | 51.6 ms                                                    | 53.4 ms: 1.03x slower                                                     |
| django_template            | 34.8 ms                                                    | 36.0 ms: 1.03x slower                                                     |
| async_generators           | 442 ms                                                     | 459 ms: 1.04x slower                                                      |
| nqueens                    | 81.4 ms                                                    | 84.8 ms: 1.04x slower                                                     |
| regex_effbot               | 3.67 ms                                                    | 3.84 ms: 1.05x slower                                                     |
| hexiom                     | 6.30 ms                                                    | 6.64 ms: 1.05x slower                                                     |
| sympy_str                  | 282 ms                                                     | 298 ms: 1.06x slower                                                      |
| deltablue                  | 3.25 ms                                                    | 3.48 ms: 1.07x slower                                                     |
| sympy_expand               | 473 ms                                                     | 508 ms: 1.07x slower                                                      |
| sympy_sum                  | 156 ms                                                     | 170 ms: 1.09x slower                                                      |
| sympy_integrate            | 20.5 ms                                                    | 22.5 ms: 1.10x slower                                                     |
| generators                 | 29.6 ms                                                    | 33.1 ms: 1.12x slower                                                     |
| pylint                     | 317 ms                                                     | 355 ms: 1.12x slower                                                      |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                              |

Benchmark hidden because not significant (2): unpickle_pure_python, 2to3
Ignored benchmarks (14) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x