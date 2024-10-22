# Results vs. 3.13.0

- fork: brandtbucher
- ref: tracing_jumps
- machine: linux-x86_64
- commit hash: f1f5d13
- commit date: 2024-07-24
- overall geometric mean: 1.01x faster
- HPT reliability: 60.28%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 276 ms: 1.04x slower                                                 |
| docutils       | 2.58 sec                                               | 2.90 sec: 1.12x slower                                               |
| html5lib       | 64.5 ms                                                | 65.9 ms: 1.02x slower                                                |
| tornado_http   | 91.5 ms                                                | 93.7 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                  | 1.05x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 389 ms: 1.20x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 402 ms: 1.10x faster                                                 |
| async_tree_none            | 354 ms                                                 | 325 ms: 1.09x faster                                                 |
| async_tree_none_tg         | 320 ms                                                 | 299 ms: 1.07x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 529 ms: 1.03x faster                                                 |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 563 ms: 1.02x faster                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                               |
| asyncio_tcp                | 488 ms                                                 | 504 ms: 1.03x slower                                                 |
| async_tree_io_tg           | 825 ms                                                 | 863 ms: 1.05x slower                                                 |
| async_generators           | 433 ms                                                 | 454 ms: 1.05x slower                                                 |
| async_tree_io              | 843 ms                                                 | 899 ms: 1.07x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                         |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.6 ms: 1.11x faster                                                |
| nbody          | 85.7 ms                                                | 80.2 ms: 1.07x faster                                                |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.97 ms: 1.02x slower                                                |
| regex_compile  | 131 ms                                                 | 134 ms: 1.02x slower                                                 |
| regex_v8       | 25.3 ms                                                | 26.4 ms: 1.04x slower                                                |
| regex_dna      | 220 ms                                                 | 237 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 79.3 ms: 1.10x faster                                                |
| tomli_loads          | 2.11 sec                                               | 1.94 sec: 1.09x faster                                               |
| xml_etree_process    | 60.4 ms                                                | 56.2 ms: 1.07x faster                                                |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 102 ms                                                 | 99.1 ms: 1.03x faster                                                |
| pickle_pure_python   | 300 us                                                 | 294 us: 1.02x faster                                                 |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                |
| unpickle_pure_python | 213 us                                                 | 216 us: 1.01x slower                                                 |
| json_loads           | 27.0 us                                                | 28.2 us: 1.04x slower                                                |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                |
| python_startup_no_site | 6.99 ms                                                | 7.20 ms: 1.03x slower                                                |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.68 ms: 1.15x faster                                                |
| django_template | 34.4 ms                                                | 36.2 ms: 1.05x slower                                                |
| genshi_xml      | 50.3 ms                                                | 53.2 ms: 1.06x slower                                                |
| genshi_text     | 22.9 ms                                                | 24.2 ms: 1.06x slower                                                |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240724-linux-x86_64-brandtbucher-tracing_jumps-3.14.0a0-f1f5d13 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 28.6 us: 1.33x faster                                                |
| deepcopy                   | 352 us                                                 | 273 us: 1.29x faster                                                 |
| async_tree_memoization_tg  | 465 ms                                                 | 389 ms: 1.20x faster                                                 |
| richards                   | 48.1 ms                                                | 40.5 ms: 1.19x faster                                                |
| scimark_fft                | 369 ms                                                 | 312 ms: 1.18x faster                                                 |
| richards_super             | 54.4 ms                                                | 46.8 ms: 1.16x faster                                                |
| deepcopy_reduce            | 3.17 us                                                | 2.75 us: 1.15x faster                                                |
| mako                       | 11.1 ms                                                | 9.68 ms: 1.15x faster                                                |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.44 ms: 1.13x faster                                                |
| float                      | 78.5 ms                                                | 70.6 ms: 1.11x faster                                                |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.11x faster                                                 |
| scimark_monte_carlo        | 66.3 ms                                                | 60.1 ms: 1.10x faster                                                |
| async_tree_memoization     | 442 ms                                                 | 402 ms: 1.10x faster                                                 |
| xml_etree_generate         | 87.0 ms                                                | 79.3 ms: 1.10x faster                                                |
| tomli_loads                | 2.11 sec                                               | 1.94 sec: 1.09x faster                                               |
| async_tree_none            | 354 ms                                                 | 325 ms: 1.09x faster                                                 |
| pyflate                    | 460 ms                                                 | 424 ms: 1.08x faster                                                 |
| crypto_pyaes               | 73.0 ms                                                | 67.4 ms: 1.08x faster                                                |
| mdp                        | 2.74 sec                                               | 2.54 sec: 1.08x faster                                               |
| telco                      | 8.45 ms                                                | 7.84 ms: 1.08x faster                                                |
| xml_etree_process          | 60.4 ms                                                | 56.2 ms: 1.07x faster                                                |
| async_tree_none_tg         | 320 ms                                                 | 299 ms: 1.07x faster                                                 |
| nbody                      | 85.7 ms                                                | 80.2 ms: 1.07x faster                                                |
| xml_etree_parse            | 156 ms                                                 | 147 ms: 1.06x faster                                                 |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                |
| gc_traversal               | 3.81 ms                                                | 3.62 ms: 1.05x faster                                                |
| bpe_tokeniser              | 4.69 sec                                               | 4.50 sec: 1.04x faster                                               |
| xml_etree_iterparse        | 102 ms                                                 | 99.1 ms: 1.03x faster                                                |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 529 ms: 1.03x faster                                                 |
| meteor_contest             | 108 ms                                                 | 105 ms: 1.02x faster                                                 |
| pycparser                  | 1.19 sec                                               | 1.17 sec: 1.02x faster                                               |
| json                       | 5.20 ms                                                | 5.09 ms: 1.02x faster                                                |
| pickle_pure_python         | 300 us                                                 | 294 us: 1.02x faster                                                 |
| fannkuch                   | 381 ms                                                 | 373 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 563 ms: 1.02x faster                                                 |
| logging_format             | 6.25 us                                                | 6.14 us: 1.02x faster                                                |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                |
| comprehensions             | 16.4 us                                                | 16.1 us: 1.02x faster                                                |
| pprint_safe_repr           | 744 ms                                                 | 734 ms: 1.01x faster                                                 |
| chaos                      | 58.4 ms                                                | 57.7 ms: 1.01x faster                                                |
| thrift                     | 796 us                                                 | 790 us: 1.01x faster                                                 |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                 |
| bench_thread_pool          | 815 us                                                 | 818 us: 1.00x slower                                                 |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.01x slower                                                |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                               |
| unpickle_pure_python       | 213 us                                                 | 216 us: 1.01x slower                                                 |
| logging_silent             | 102 ns                                                 | 103 ns: 1.01x slower                                                 |
| raytrace                   | 262 ms                                                 | 266 ms: 1.02x slower                                                 |
| html5lib                   | 64.5 ms                                                | 65.9 ms: 1.02x slower                                                |
| regex_effbot               | 3.88 ms                                                | 3.97 ms: 1.02x slower                                                |
| regex_compile              | 131 ms                                                 | 134 ms: 1.02x slower                                                 |
| tornado_http               | 91.5 ms                                                | 93.7 ms: 1.02x slower                                                |
| sqlglot_parse              | 1.27 ms                                                | 1.30 ms: 1.03x slower                                                |
| python_startup_no_site     | 6.99 ms                                                | 7.20 ms: 1.03x slower                                                |
| go                         | 142 ms                                                 | 146 ms: 1.03x slower                                                 |
| asyncio_tcp                | 488 ms                                                 | 504 ms: 1.03x slower                                                 |
| sqlglot_optimize           | 53.9 ms                                                | 55.8 ms: 1.03x slower                                                |
| sqlglot_transpile          | 1.57 ms                                                | 1.63 ms: 1.03x slower                                                |
| nqueens                    | 80.6 ms                                                | 83.6 ms: 1.04x slower                                                |
| 2to3                       | 265 ms                                                 | 276 ms: 1.04x slower                                                 |
| regex_v8                   | 25.3 ms                                                | 26.4 ms: 1.04x slower                                                |
| json_loads                 | 27.0 us                                                | 28.2 us: 1.04x slower                                                |
| async_tree_io_tg           | 825 ms                                                 | 863 ms: 1.05x slower                                                 |
| async_generators           | 433 ms                                                 | 454 ms: 1.05x slower                                                 |
| django_template            | 34.4 ms                                                | 36.2 ms: 1.05x slower                                                |
| typing_runtime_protocols   | 159 us                                                 | 168 us: 1.05x slower                                                 |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.06x slower                                                 |
| genshi_xml                 | 50.3 ms                                                | 53.2 ms: 1.06x slower                                                |
| genshi_text                | 22.9 ms                                                | 24.2 ms: 1.06x slower                                                |
| scimark_sor                | 122 ms                                                 | 130 ms: 1.06x slower                                                 |
| async_tree_io              | 843 ms                                                 | 899 ms: 1.07x slower                                                 |
| dask                       | 338 ms                                                 | 362 ms: 1.07x slower                                                 |
| regex_dna                  | 220 ms                                                 | 237 ms: 1.08x slower                                                 |
| scimark_lu                 | 115 ms                                                 | 124 ms: 1.08x slower                                                 |
| sympy_str                  | 274 ms                                                 | 297 ms: 1.08x slower                                                 |
| sympy_expand               | 462 ms                                                 | 504 ms: 1.09x slower                                                 |
| coverage                   | 83.7 ms                                                | 91.5 ms: 1.09x slower                                                |
| create_gc_cycles           | 1.61 ms                                                | 1.76 ms: 1.10x slower                                                |
| hexiom                     | 6.13 ms                                                | 6.74 ms: 1.10x slower                                                |
| dulwich_log                | 63.0 ms                                                | 69.9 ms: 1.11x slower                                                |
| docutils                   | 2.58 sec                                               | 2.90 sec: 1.12x slower                                               |
| sympy_integrate            | 19.9 ms                                                | 22.4 ms: 1.13x slower                                                |
| sympy_sum                  | 150 ms                                                 | 169 ms: 1.13x slower                                                 |
| deltablue                  | 3.15 ms                                                | 3.56 ms: 1.13x slower                                                |
| pylint                     | 313 ms                                                 | 354 ms: 1.13x slower                                                 |
| generators                 | 28.8 ms                                                | 32.8 ms: 1.14x slower                                                |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (5): logging_simple, pprint_pformat, bench_mp_pool, asyncio_websockets, coroutines
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 60.28% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x