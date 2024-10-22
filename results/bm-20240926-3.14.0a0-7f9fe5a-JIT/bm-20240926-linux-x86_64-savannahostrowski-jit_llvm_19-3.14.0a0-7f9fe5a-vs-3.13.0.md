# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: linux-x86_64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.00x faster
- HPT reliability: 62.42%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 274 ms: 1.04x slower                                                    |
| docutils       | 2.58 sec                                               | 2.94 sec: 1.14x slower                                                  |
| html5lib       | 64.5 ms                                                | 62.0 ms: 1.04x faster                                                   |
| tornado_http   | 91.5 ms                                                | 94.6 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 388 ms: 1.20x faster                                                    |
| async_tree_none            | 354 ms                                                 | 315 ms: 1.12x faster                                                    |
| async_tree_memoization     | 442 ms                                                 | 397 ms: 1.11x faster                                                    |
| async_tree_none_tg         | 320 ms                                                 | 308 ms: 1.04x faster                                                    |
| asyncio_tcp                | 488 ms                                                 | 491 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                  |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 556 ms: 1.02x slower                                                    |
| async_generators           | 433 ms                                                 | 455 ms: 1.05x slower                                                    |
| async_tree_io              | 843 ms                                                 | 885 ms: 1.05x slower                                                    |
| async_tree_io_tg           | 825 ms                                                 | 875 ms: 1.06x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                            |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.1 ms: 1.12x faster                                                   |
| nbody          | 85.7 ms                                                | 81.8 ms: 1.05x faster                                                   |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                  | 1.05x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                | 24.2 ms: 1.04x faster                                                   |
| regex_effbot   | 3.88 ms                                                | 3.72 ms: 1.04x faster                                                   |
| regex_dna      | 220 ms                                                 | 212 ms: 1.04x faster                                                    |
| regex_compile  | 131 ms                                                 | 142 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 78.1 ms: 1.11x faster                                                   |
| xml_etree_process    | 60.4 ms                                                | 55.0 ms: 1.10x faster                                                   |
| tomli_loads          | 2.11 sec                                               | 1.96 sec: 1.08x faster                                                  |
| xml_etree_parse      | 156 ms                                                 | 147 ms: 1.06x faster                                                    |
| xml_etree_iterparse  | 102 ms                                                 | 98.6 ms: 1.04x faster                                                   |
| json_dumps           | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                   |
| pickle               | 11.6 us                                                | 11.6 us: 1.00x slower                                                   |
| pickle_dict          | 33.2 us                                                | 33.3 us: 1.00x slower                                                   |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                    |
| json_loads           | 27.0 us                                                | 27.2 us: 1.01x slower                                                   |
| pickle_pure_python   | 300 us                                                 | 307 us: 1.02x slower                                                    |
| pickle_list          | 5.01 us                                                | 5.20 us: 1.04x slower                                                   |
| unpickle_list        | 4.96 us                                                | 5.30 us: 1.07x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                            |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                   |
| python_startup_no_site | 6.99 ms                                                | 7.08 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.1 ms: 1.10x faster                                                   |
| django_template | 34.4 ms                                                | 35.5 ms: 1.03x slower                                                   |
| genshi_text     | 22.9 ms                                                | 24.4 ms: 1.07x slower                                                   |
| genshi_xml      | 50.3 ms                                                | 57.2 ms: 1.14x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240926-linux-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 26.7 us: 1.42x faster                                                   |
| deepcopy                   | 352 us                                                 | 261 us: 1.35x faster                                                    |
| richards_super             | 54.4 ms                                                | 44.9 ms: 1.21x faster                                                   |
| richards                   | 48.1 ms                                                | 39.8 ms: 1.21x faster                                                   |
| async_tree_memoization_tg  | 465 ms                                                 | 388 ms: 1.20x faster                                                    |
| deepcopy_reduce            | 3.17 us                                                | 2.65 us: 1.20x faster                                                   |
| scimark_fft                | 369 ms                                                 | 312 ms: 1.18x faster                                                    |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.39 ms: 1.14x faster                                                   |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                                    |
| async_tree_none            | 354 ms                                                 | 315 ms: 1.12x faster                                                    |
| float                      | 78.5 ms                                                | 70.1 ms: 1.12x faster                                                   |
| async_tree_memoization     | 442 ms                                                 | 397 ms: 1.11x faster                                                    |
| xml_etree_generate         | 87.0 ms                                                | 78.1 ms: 1.11x faster                                                   |
| mako                       | 11.1 ms                                                | 10.1 ms: 1.10x faster                                                   |
| xml_etree_process          | 60.4 ms                                                | 55.0 ms: 1.10x faster                                                   |
| crypto_pyaes               | 73.0 ms                                                | 66.8 ms: 1.09x faster                                                   |
| tomli_loads                | 2.11 sec                                               | 1.96 sec: 1.08x faster                                                  |
| go                         | 142 ms                                                 | 132 ms: 1.08x faster                                                    |
| telco                      | 8.45 ms                                                | 7.86 ms: 1.08x faster                                                   |
| pathlib                    | 17.1 ms                                                | 15.9 ms: 1.07x faster                                                   |
| xml_etree_parse            | 156 ms                                                 | 147 ms: 1.06x faster                                                    |
| scimark_monte_carlo        | 66.3 ms                                                | 62.8 ms: 1.05x faster                                                   |
| mdp                        | 2.74 sec                                               | 2.60 sec: 1.05x faster                                                  |
| bpe_tokeniser              | 4.69 sec                                               | 4.45 sec: 1.05x faster                                                  |
| scimark_lu                 | 115 ms                                                 | 109 ms: 1.05x faster                                                    |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.05x faster                                                    |
| nbody                      | 85.7 ms                                                | 81.8 ms: 1.05x faster                                                   |
| regex_v8                   | 25.3 ms                                                | 24.2 ms: 1.04x faster                                                   |
| regex_effbot               | 3.88 ms                                                | 3.72 ms: 1.04x faster                                                   |
| sqlite_synth               | 2.85 us                                                | 2.74 us: 1.04x faster                                                   |
| html5lib                   | 64.5 ms                                                | 62.0 ms: 1.04x faster                                                   |
| async_tree_none_tg         | 320 ms                                                 | 308 ms: 1.04x faster                                                    |
| xml_etree_iterparse        | 102 ms                                                 | 98.6 ms: 1.04x faster                                                   |
| regex_dna                  | 220 ms                                                 | 212 ms: 1.04x faster                                                    |
| logging_format             | 6.25 us                                                | 6.05 us: 1.03x faster                                                   |
| json_dumps                 | 10.4 ms                                                | 10.1 ms: 1.03x faster                                                   |
| pycparser                  | 1.19 sec                                               | 1.16 sec: 1.03x faster                                                  |
| json                       | 5.20 ms                                                | 5.11 ms: 1.02x faster                                                   |
| logging_simple             | 5.66 us                                                | 5.58 us: 1.01x faster                                                   |
| thrift                     | 796 us                                                 | 787 us: 1.01x faster                                                    |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.00x faster                                                    |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                   |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                    |
| pickle                     | 11.6 us                                                | 11.6 us: 1.00x slower                                                   |
| pickle_dict                | 33.2 us                                                | 33.3 us: 1.00x slower                                                   |
| asyncio_tcp                | 488 ms                                                 | 491 ms: 1.01x slower                                                    |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                                    |
| fannkuch                   | 381 ms                                                 | 384 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                                  |
| json_loads                 | 27.0 us                                                | 27.2 us: 1.01x slower                                                   |
| deltablue                  | 3.15 ms                                                | 3.19 ms: 1.01x slower                                                   |
| coverage                   | 83.7 ms                                                | 84.8 ms: 1.01x slower                                                   |
| python_startup_no_site     | 6.99 ms                                                | 7.08 ms: 1.01x slower                                                   |
| typing_runtime_protocols   | 159 us                                                 | 162 us: 1.02x slower                                                    |
| pprint_pformat             | 1.51 sec                                               | 1.54 sec: 1.02x slower                                                  |
| chaos                      | 58.4 ms                                                | 59.7 ms: 1.02x slower                                                   |
| coroutines                 | 22.5 ms                                                | 23.0 ms: 1.02x slower                                                   |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                    |
| pickle_pure_python         | 300 us                                                 | 307 us: 1.02x slower                                                    |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 556 ms: 1.02x slower                                                    |
| django_template            | 34.4 ms                                                | 35.5 ms: 1.03x slower                                                   |
| bench_thread_pool          | 815 us                                                 | 841 us: 1.03x slower                                                    |
| tornado_http               | 91.5 ms                                                | 94.6 ms: 1.03x slower                                                   |
| 2to3                       | 265 ms                                                 | 274 ms: 1.04x slower                                                    |
| pprint_safe_repr           | 744 ms                                                 | 772 ms: 1.04x slower                                                    |
| pickle_list                | 5.01 us                                                | 5.20 us: 1.04x slower                                                   |
| sqlglot_normalize          | 107 ms                                                 | 112 ms: 1.04x slower                                                    |
| gc_traversal               | 3.81 ms                                                | 3.97 ms: 1.04x slower                                                   |
| sqlglot_parse              | 1.27 ms                                                | 1.33 ms: 1.05x slower                                                   |
| async_generators           | 433 ms                                                 | 455 ms: 1.05x slower                                                    |
| async_tree_io              | 843 ms                                                 | 885 ms: 1.05x slower                                                    |
| raytrace                   | 262 ms                                                 | 276 ms: 1.06x slower                                                    |
| async_tree_io_tg           | 825 ms                                                 | 875 ms: 1.06x slower                                                    |
| nqueens                    | 80.6 ms                                                | 85.6 ms: 1.06x slower                                                   |
| sqlglot_transpile          | 1.57 ms                                                | 1.67 ms: 1.06x slower                                                   |
| genshi_text                | 22.9 ms                                                | 24.4 ms: 1.07x slower                                                   |
| unpickle_list              | 4.96 us                                                | 5.30 us: 1.07x slower                                                   |
| sqlglot_optimize           | 53.9 ms                                                | 57.7 ms: 1.07x slower                                                   |
| dulwich_log                | 63.0 ms                                                | 67.9 ms: 1.08x slower                                                   |
| regex_compile              | 131 ms                                                 | 142 ms: 1.09x slower                                                    |
| sympy_expand               | 462 ms                                                 | 502 ms: 1.09x slower                                                    |
| sympy_str                  | 274 ms                                                 | 298 ms: 1.09x slower                                                    |
| create_gc_cycles           | 1.61 ms                                                | 1.76 ms: 1.09x slower                                                   |
| hexiom                     | 6.13 ms                                                | 6.87 ms: 1.12x slower                                                   |
| docutils                   | 2.58 sec                                               | 2.94 sec: 1.14x slower                                                  |
| genshi_xml                 | 50.3 ms                                                | 57.2 ms: 1.14x slower                                                   |
| sympy_integrate            | 19.9 ms                                                | 22.7 ms: 1.14x slower                                                   |
| generators                 | 28.8 ms                                                | 33.1 ms: 1.15x slower                                                   |
| sympy_sum                  | 150 ms                                                 | 172 ms: 1.15x slower                                                    |
| pylint                     | 313 ms                                                 | 370 ms: 1.18x slower                                                    |
| unpack_sequence            | 42.4 ns                                                | 112 ns: 2.64x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                            |

Benchmark hidden because not significant (6): unpickle, pyflate, async_tree_cpu_io_mixed, asyncio_websockets, comprehensions, bench_mp_pool
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 62.42% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x