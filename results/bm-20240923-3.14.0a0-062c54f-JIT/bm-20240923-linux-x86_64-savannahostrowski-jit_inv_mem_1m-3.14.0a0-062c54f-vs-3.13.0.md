# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_inv_mem_1m
- machine: linux-x86_64
- commit hash: 062c54f
- commit date: 2024-09-23
- overall geometric mean: 1.00x slower
- HPT reliability: 71.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 277 ms: 1.04x slower                                                       |
| docutils       | 2.58 sec                                               | 2.93 sec: 1.14x slower                                                     |
| html5lib       | 64.5 ms                                                | 64.3 ms: 1.00x faster                                                      |
| tornado_http   | 91.5 ms                                                | 95.0 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.05x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 389 ms: 1.20x faster                                                       |
| async_tree_none            | 354 ms                                                 | 313 ms: 1.13x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 396 ms: 1.12x faster                                                       |
| async_tree_none_tg         | 320 ms                                                 | 307 ms: 1.04x faster                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                     |
| asyncio_tcp                | 488 ms                                                 | 496 ms: 1.02x slower                                                       |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 555 ms: 1.02x slower                                                       |
| async_tree_io_tg           | 825 ms                                                 | 872 ms: 1.06x slower                                                       |
| async_generators           | 433 ms                                                 | 459 ms: 1.06x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 69.6 ms: 1.13x faster                                                      |
| nbody          | 85.7 ms                                                | 84.1 ms: 1.02x faster                                                      |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 24.6 ms: 1.03x faster                                                      |
| regex_effbot   | 3.88 ms                                                | 3.80 ms: 1.02x faster                                                      |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                                       |
| regex_compile  | 131 ms                                                 | 143 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 77.8 ms: 1.12x faster                                                      |
| xml_etree_process    | 60.4 ms                                                | 54.5 ms: 1.11x faster                                                      |
| tomli_loads          | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                     |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                       |
| json_dumps           | 10.4 ms                                                | 9.93 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 102 ms                                                 | 98.4 ms: 1.04x faster                                                      |
| unpickle             | 14.9 us                                                | 14.5 us: 1.02x faster                                                      |
| pickle_pure_python   | 300 us                                                 | 304 us: 1.01x slower                                                       |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                       |
| pickle_list          | 5.01 us                                                | 5.10 us: 1.02x slower                                                      |
| json_loads           | 27.0 us                                                | 27.6 us: 1.02x slower                                                      |
| pickle_dict          | 33.2 us                                                | 34.5 us: 1.04x slower                                                      |
| unpickle_list        | 4.96 us                                                | 5.29 us: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                      |
| python_startup_no_site | 6.99 ms                                                | 7.05 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.87 ms: 1.12x faster                                                      |
| django_template | 34.4 ms                                                | 36.7 ms: 1.07x slower                                                      |
| genshi_text     | 22.9 ms                                                | 24.9 ms: 1.09x slower                                                      |
| genshi_xml      | 50.3 ms                                                | 58.7 ms: 1.17x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_1m-3.14.0a0-062c54f |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 27.1 us: 1.40x faster                                                      |
| deepcopy                   | 352 us                                                 | 263 us: 1.34x faster                                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 389 ms: 1.20x faster                                                       |
| deepcopy_reduce            | 3.17 us                                                | 2.68 us: 1.18x faster                                                      |
| richards                   | 48.1 ms                                                | 40.7 ms: 1.18x faster                                                      |
| scimark_fft                | 369 ms                                                 | 312 ms: 1.18x faster                                                       |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.26 ms: 1.18x faster                                                      |
| richards_super             | 54.4 ms                                                | 46.7 ms: 1.16x faster                                                      |
| async_tree_none            | 354 ms                                                 | 313 ms: 1.13x faster                                                       |
| float                      | 78.5 ms                                                | 69.6 ms: 1.13x faster                                                      |
| mako                       | 11.1 ms                                                | 9.87 ms: 1.12x faster                                                      |
| xml_etree_generate         | 87.0 ms                                                | 77.8 ms: 1.12x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 396 ms: 1.12x faster                                                       |
| xml_etree_process          | 60.4 ms                                                | 54.5 ms: 1.11x faster                                                      |
| spectral_norm              | 115 ms                                                 | 105 ms: 1.09x faster                                                       |
| crypto_pyaes               | 73.0 ms                                                | 66.7 ms: 1.09x faster                                                      |
| tomli_loads                | 2.11 sec                                               | 1.94 sec: 1.09x faster                                                     |
| pathlib                    | 17.1 ms                                                | 15.9 ms: 1.07x faster                                                      |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                       |
| mdp                        | 2.74 sec                                               | 2.59 sec: 1.06x faster                                                     |
| go                         | 142 ms                                                 | 134 ms: 1.06x faster                                                       |
| json_dumps                 | 10.4 ms                                                | 9.93 ms: 1.05x faster                                                      |
| bpe_tokeniser              | 4.69 sec                                               | 4.48 sec: 1.05x faster                                                     |
| scimark_monte_carlo        | 66.3 ms                                                | 63.3 ms: 1.05x faster                                                      |
| telco                      | 8.45 ms                                                | 8.08 ms: 1.05x faster                                                      |
| async_tree_none_tg         | 320 ms                                                 | 307 ms: 1.04x faster                                                       |
| scimark_lu                 | 115 ms                                                 | 111 ms: 1.04x faster                                                       |
| gc_traversal               | 3.81 ms                                                | 3.66 ms: 1.04x faster                                                      |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.04x faster                                                       |
| xml_etree_iterparse        | 102 ms                                                 | 98.4 ms: 1.04x faster                                                      |
| sqlite_synth               | 2.85 us                                                | 2.75 us: 1.04x faster                                                      |
| regex_v8                   | 25.3 ms                                                | 24.6 ms: 1.03x faster                                                      |
| unpickle                   | 14.9 us                                                | 14.5 us: 1.02x faster                                                      |
| regex_effbot               | 3.88 ms                                                | 3.80 ms: 1.02x faster                                                      |
| nbody                      | 85.7 ms                                                | 84.1 ms: 1.02x faster                                                      |
| thrift                     | 796 us                                                 | 782 us: 1.02x faster                                                       |
| logging_format             | 6.25 us                                                | 6.15 us: 1.02x faster                                                      |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                                       |
| logging_simple             | 5.66 us                                                | 5.59 us: 1.01x faster                                                      |
| pyflate                    | 460 ms                                                 | 454 ms: 1.01x faster                                                       |
| fannkuch                   | 381 ms                                                 | 379 ms: 1.01x faster                                                       |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                      |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.00x faster                                                       |
| pidigits                   | 186 ms                                                 | 185 ms: 1.00x faster                                                       |
| html5lib                   | 64.5 ms                                                | 64.3 ms: 1.00x faster                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.00x slower                                                     |
| chaos                      | 58.4 ms                                                | 58.9 ms: 1.01x slower                                                      |
| python_startup_no_site     | 6.99 ms                                                | 7.05 ms: 1.01x slower                                                      |
| pickle_pure_python         | 300 us                                                 | 304 us: 1.01x slower                                                       |
| coverage                   | 83.7 ms                                                | 85.0 ms: 1.01x slower                                                      |
| asyncio_tcp                | 488 ms                                                 | 496 ms: 1.02x slower                                                       |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                       |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                      |
| pickle_list                | 5.01 us                                                | 5.10 us: 1.02x slower                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 555 ms: 1.02x slower                                                       |
| json_loads                 | 27.0 us                                                | 27.6 us: 1.02x slower                                                      |
| deltablue                  | 3.15 ms                                                | 3.23 ms: 1.02x slower                                                      |
| comprehensions             | 16.4 us                                                | 16.9 us: 1.03x slower                                                      |
| bench_thread_pool          | 815 us                                                 | 839 us: 1.03x slower                                                       |
| tornado_http               | 91.5 ms                                                | 95.0 ms: 1.04x slower                                                      |
| pickle_dict                | 33.2 us                                                | 34.5 us: 1.04x slower                                                      |
| typing_runtime_protocols   | 159 us                                                 | 166 us: 1.04x slower                                                       |
| 2to3                       | 265 ms                                                 | 277 ms: 1.04x slower                                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.33 ms: 1.05x slower                                                      |
| raytrace                   | 262 ms                                                 | 276 ms: 1.05x slower                                                       |
| async_tree_io_tg           | 825 ms                                                 | 872 ms: 1.06x slower                                                       |
| sqlglot_normalize          | 107 ms                                                 | 114 ms: 1.06x slower                                                       |
| async_generators           | 433 ms                                                 | 459 ms: 1.06x slower                                                       |
| unpickle_list              | 4.96 us                                                | 5.29 us: 1.07x slower                                                      |
| django_template            | 34.4 ms                                                | 36.7 ms: 1.07x slower                                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.70 ms: 1.08x slower                                                      |
| create_gc_cycles           | 1.61 ms                                                | 1.74 ms: 1.08x slower                                                      |
| dulwich_log                | 63.0 ms                                                | 68.2 ms: 1.08x slower                                                      |
| sqlglot_optimize           | 53.9 ms                                                | 58.6 ms: 1.09x slower                                                      |
| genshi_text                | 22.9 ms                                                | 24.9 ms: 1.09x slower                                                      |
| regex_compile              | 131 ms                                                 | 143 ms: 1.09x slower                                                       |
| nqueens                    | 80.6 ms                                                | 89.0 ms: 1.10x slower                                                      |
| sympy_expand               | 462 ms                                                 | 514 ms: 1.11x slower                                                       |
| sympy_str                  | 274 ms                                                 | 305 ms: 1.12x slower                                                       |
| docutils                   | 2.58 sec                                               | 2.93 sec: 1.14x slower                                                     |
| hexiom                     | 6.13 ms                                                | 6.97 ms: 1.14x slower                                                      |
| sympy_integrate            | 19.9 ms                                                | 23.0 ms: 1.16x slower                                                      |
| genshi_xml                 | 50.3 ms                                                | 58.7 ms: 1.17x slower                                                      |
| sympy_sum                  | 150 ms                                                 | 174 ms: 1.17x slower                                                       |
| pylint                     | 313 ms                                                 | 378 ms: 1.21x slower                                                       |
| generators                 | 28.8 ms                                                | 34.9 ms: 1.21x slower                                                      |
| unpack_sequence            | 42.4 ns                                                | 105 ns: 2.47x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (10): pycparser, async_tree_cpu_io_mixed, pickle, asyncio_websockets, bench_mp_pool, pprint_safe_repr, json, pprint_pformat, logging_silent, async_tree_io
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 71.90% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x