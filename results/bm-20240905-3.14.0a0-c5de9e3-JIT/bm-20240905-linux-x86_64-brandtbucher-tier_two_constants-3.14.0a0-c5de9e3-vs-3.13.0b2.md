# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: c5de9e3
- commit date: 2024-09-05
- overall geometric mean: 1.05x faster
- HPT reliability: 99.89%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 2.83 sec                                                   | 3.02 sec: 1.07x slower                                                    |
| html5lib       | 67.2 ms                                                    | 64.3 ms: 1.04x faster                                                     |
| tornado_http   | 94.6 ms                                                    | 95.5 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                      | 1.01x slower                                                              |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization     | 463 ms                                                     | 401 ms: 1.16x faster                                                      |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                      |
| async_tree_memoization_tg  | 444 ms                                                     | 402 ms: 1.10x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 556 ms: 1.10x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 538 ms: 1.09x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 311 ms: 1.08x faster                                                      |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                              |

Benchmark hidden because not significant (2): async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.9 ms                                                    | 71.4 ms: 1.10x faster                                                     |
| nbody          | 88.3 ms                                                    | 80.7 ms: 1.09x faster                                                     |
| pidigits       | 191 ms                                                     | 187 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                      | 1.07x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                     |
| regex_dna      | 221 ms                                                     | 215 ms: 1.03x faster                                                      |
| regex_effbot   | 3.67 ms                                                    | 3.64 ms: 1.01x faster                                                     |
| regex_compile  | 137 ms                                                     | 140 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                      | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate   | 87.4 ms                                                    | 77.6 ms: 1.13x faster                                                     |
| xml_etree_process    | 61.2 ms                                                    | 54.7 ms: 1.12x faster                                                     |
| tomli_loads          | 2.12 sec                                                   | 1.92 sec: 1.11x faster                                                    |
| xml_etree_parse      | 162 ms                                                     | 148 ms: 1.10x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                     | 98.6 ms: 1.09x faster                                                     |
| json_dumps           | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                     |
| unpickle_pure_python | 218 us                                                     | 211 us: 1.03x faster                                                      |
| pickle_pure_python   | 305 us                                                     | 298 us: 1.03x faster                                                      |
| json_loads           | 28.9 us                                                    | 28.6 us: 1.01x faster                                                     |
| Geometric mean       | (ref)                                                      | 1.07x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                     |
| python_startup_no_site | 7.11 ms                                                    | 7.18 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                      | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 9.86 ms: 1.14x faster                                                     |
| django_template | 34.8 ms                                                    | 35.5 ms: 1.02x slower                                                     |
| genshi_text     | 23.7 ms                                                    | 24.9 ms: 1.05x slower                                                     |
| genshi_xml      | 51.6 ms                                                    | 59.4 ms: 1.15x slower                                                     |
| Geometric mean  | (ref)                                                      | 1.02x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240905-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-c5de9e3 |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 39.7 us                                                    | 26.6 us: 1.49x faster                                                     |
| deepcopy                   | 367 us                                                     | 266 us: 1.38x faster                                                      |
| richards                   | 50.9 ms                                                    | 39.1 ms: 1.30x faster                                                     |
| scimark_fft                | 392 ms                                                     | 307 ms: 1.28x faster                                                      |
| richards_super             | 57.4 ms                                                    | 44.9 ms: 1.28x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                    | 2.65 us: 1.26x faster                                                     |
| spectral_norm              | 116 ms                                                     | 99.1 ms: 1.17x faster                                                     |
| crypto_pyaes               | 77.5 ms                                                    | 66.2 ms: 1.17x faster                                                     |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.55 ms: 1.16x faster                                                     |
| async_tree_memoization     | 463 ms                                                     | 401 ms: 1.16x faster                                                      |
| async_tree_none            | 378 ms                                                     | 327 ms: 1.16x faster                                                      |
| mako                       | 11.2 ms                                                    | 9.86 ms: 1.14x faster                                                     |
| bpe_tokeniser              | 5.02 sec                                                   | 4.41 sec: 1.14x faster                                                    |
| xml_etree_generate         | 87.4 ms                                                    | 77.6 ms: 1.13x faster                                                     |
| xml_etree_process          | 61.2 ms                                                    | 54.7 ms: 1.12x faster                                                     |
| go                         | 145 ms                                                     | 130 ms: 1.12x faster                                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 62.5 ms: 1.11x faster                                                     |
| tomli_loads                | 2.12 sec                                                   | 1.92 sec: 1.11x faster                                                    |
| float                      | 78.9 ms                                                    | 71.4 ms: 1.10x faster                                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 402 ms: 1.10x faster                                                      |
| mdp                        | 2.79 sec                                                   | 2.53 sec: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 556 ms: 1.10x faster                                                      |
| gc_traversal               | 3.98 ms                                                    | 3.62 ms: 1.10x faster                                                     |
| scimark_sor                | 127 ms                                                     | 116 ms: 1.10x faster                                                      |
| xml_etree_parse            | 162 ms                                                     | 148 ms: 1.10x faster                                                      |
| nbody                      | 88.3 ms                                                    | 80.7 ms: 1.09x faster                                                     |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 538 ms: 1.09x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                     | 98.6 ms: 1.09x faster                                                     |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.09x faster                                                     |
| async_tree_none_tg         | 336 ms                                                     | 311 ms: 1.08x faster                                                      |
| fannkuch                   | 402 ms                                                     | 372 ms: 1.08x faster                                                      |
| scimark_lu                 | 122 ms                                                     | 113 ms: 1.07x faster                                                      |
| pyflate                    | 484 ms                                                     | 451 ms: 1.07x faster                                                      |
| telco                      | 8.41 ms                                                    | 7.89 ms: 1.07x faster                                                     |
| pprint_safe_repr           | 758 ms                                                     | 713 ms: 1.06x faster                                                      |
| thrift                     | 823 us                                                     | 776 us: 1.06x faster                                                      |
| logging_silent             | 105 ns                                                     | 99.5 ns: 1.05x faster                                                     |
| chaos                      | 61.3 ms                                                    | 58.3 ms: 1.05x faster                                                     |
| pprint_pformat             | 1.56 sec                                                   | 1.49 sec: 1.05x faster                                                    |
| html5lib                   | 67.2 ms                                                    | 64.3 ms: 1.04x faster                                                     |
| asyncio_tcp                | 508 ms                                                     | 488 ms: 1.04x faster                                                      |
| logging_format             | 6.47 us                                                    | 6.24 us: 1.04x faster                                                     |
| json_dumps                 | 10.7 ms                                                    | 10.4 ms: 1.03x faster                                                     |
| unpickle_pure_python       | 218 us                                                     | 211 us: 1.03x faster                                                      |
| regex_v8                   | 25.1 ms                                                    | 24.4 ms: 1.03x faster                                                     |
| meteor_contest             | 110 ms                                                     | 107 ms: 1.03x faster                                                      |
| regex_dna                  | 221 ms                                                     | 215 ms: 1.03x faster                                                      |
| pickle_pure_python         | 305 us                                                     | 298 us: 1.03x faster                                                      |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.80 sec: 1.02x faster                                                    |
| coroutines                 | 23.2 ms                                                    | 22.7 ms: 1.02x faster                                                     |
| asyncio_websockets         | 567 ms                                                     | 555 ms: 1.02x faster                                                      |
| deltablue                  | 3.25 ms                                                    | 3.19 ms: 1.02x faster                                                     |
| create_gc_cycles           | 1.82 ms                                                    | 1.78 ms: 1.02x faster                                                     |
| pidigits                   | 191 ms                                                     | 187 ms: 1.02x faster                                                      |
| logging_simple             | 5.74 us                                                    | 5.65 us: 1.02x faster                                                     |
| python_startup             | 10.8 ms                                                    | 10.6 ms: 1.02x faster                                                     |
| typing_runtime_protocols   | 165 us                                                     | 162 us: 1.01x faster                                                      |
| json_loads                 | 28.9 us                                                    | 28.6 us: 1.01x faster                                                     |
| regex_effbot               | 3.67 ms                                                    | 3.64 ms: 1.01x faster                                                     |
| bench_mp_pool              | 23.9 ms                                                    | 24.0 ms: 1.01x slower                                                     |
| comprehensions             | 16.6 us                                                    | 16.7 us: 1.01x slower                                                     |
| tornado_http               | 94.6 ms                                                    | 95.5 ms: 1.01x slower                                                     |
| sqlglot_parse              | 1.32 ms                                                    | 1.33 ms: 1.01x slower                                                     |
| coverage                   | 93.1 ms                                                    | 94.0 ms: 1.01x slower                                                     |
| python_startup_no_site     | 7.11 ms                                                    | 7.18 ms: 1.01x slower                                                     |
| dulwich_log                | 67.2 ms                                                    | 68.1 ms: 1.01x slower                                                     |
| pycparser                  | 1.16 sec                                                   | 1.18 sec: 1.02x slower                                                    |
| sqlglot_normalize          | 110 ms                                                     | 112 ms: 1.02x slower                                                      |
| django_template            | 34.8 ms                                                    | 35.5 ms: 1.02x slower                                                     |
| regex_compile              | 137 ms                                                     | 140 ms: 1.02x slower                                                      |
| async_generators           | 442 ms                                                     | 453 ms: 1.02x slower                                                      |
| sqlglot_transpile          | 1.63 ms                                                    | 1.68 ms: 1.03x slower                                                     |
| raytrace                   | 267 ms                                                     | 276 ms: 1.04x slower                                                      |
| nqueens                    | 81.4 ms                                                    | 85.2 ms: 1.05x slower                                                     |
| sqlglot_optimize           | 55.5 ms                                                    | 58.3 ms: 1.05x slower                                                     |
| genshi_text                | 23.7 ms                                                    | 24.9 ms: 1.05x slower                                                     |
| sympy_str                  | 282 ms                                                     | 300 ms: 1.06x slower                                                      |
| docutils                   | 2.83 sec                                                   | 3.02 sec: 1.07x slower                                                    |
| sympy_expand               | 473 ms                                                     | 507 ms: 1.07x slower                                                      |
| hexiom                     | 6.30 ms                                                    | 6.85 ms: 1.09x slower                                                     |
| sympy_sum                  | 156 ms                                                     | 173 ms: 1.11x slower                                                      |
| sympy_integrate            | 20.5 ms                                                    | 22.8 ms: 1.11x slower                                                     |
| generators                 | 29.6 ms                                                    | 33.1 ms: 1.12x slower                                                     |
| genshi_xml                 | 51.6 ms                                                    | 59.4 ms: 1.15x slower                                                     |
| pylint                     | 317 ms                                                     | 372 ms: 1.17x slower                                                      |
| Geometric mean             | (ref)                                                      | 1.05x faster                                                              |

Benchmark hidden because not significant (5): async_tree_io_tg, async_tree_io, bench_thread_pool, 2to3, json
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.89% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.09x