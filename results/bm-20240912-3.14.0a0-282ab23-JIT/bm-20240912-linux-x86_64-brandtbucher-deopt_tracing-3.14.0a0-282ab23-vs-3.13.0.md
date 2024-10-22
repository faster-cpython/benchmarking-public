# Results vs. 3.13.0

- fork: brandtbucher
- ref: deopt_tracing
- machine: linux-x86_64
- commit hash: 282ab23
- commit date: 2024-09-12
- overall geometric mean: 1.00x faster
- HPT reliability: 76.09%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 275 ms: 1.04x slower                                                 |
| docutils       | 2.58 sec                                               | 2.94 sec: 1.14x slower                                               |
| html5lib       | 64.5 ms                                                | 63.3 ms: 1.02x faster                                                |
| tornado_http   | 91.5 ms                                                | 94.7 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.05x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 385 ms: 1.21x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 392 ms: 1.13x faster                                                 |
| async_tree_none            | 354 ms                                                 | 314 ms: 1.13x faster                                                 |
| async_tree_none_tg         | 320 ms                                                 | 305 ms: 1.05x faster                                                 |
| coroutines                 | 22.5 ms                                                | 22.7 ms: 1.01x slower                                                |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                               |
| asyncio_tcp                | 488 ms                                                 | 496 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 553 ms: 1.02x slower                                                 |
| async_tree_io_tg           | 825 ms                                                 | 861 ms: 1.04x slower                                                 |
| async_generators           | 433 ms                                                 | 458 ms: 1.06x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                         |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, asyncio_websockets, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.0 ms: 1.12x faster                                                |
| nbody          | 85.7 ms                                                | 80.2 ms: 1.07x faster                                                |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.75 ms: 1.04x faster                                                |
| regex_v8       | 25.3 ms                                                | 25.1 ms: 1.01x faster                                                |
| regex_dna      | 220 ms                                                 | 224 ms: 1.02x slower                                                 |
| regex_compile  | 131 ms                                                 | 140 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 77.2 ms: 1.13x faster                                                |
| xml_etree_process    | 60.4 ms                                                | 54.2 ms: 1.11x faster                                                |
| tomli_loads          | 2.11 sec                                               | 1.97 sec: 1.07x faster                                               |
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                 |
| xml_etree_iterparse  | 102 ms                                                 | 98.8 ms: 1.03x faster                                                |
| unpickle             | 14.9 us                                                | 14.5 us: 1.02x faster                                                |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                |
| pickle               | 11.6 us                                                | 11.5 us: 1.01x faster                                                |
| unpickle_pure_python | 213 us                                                 | 215 us: 1.01x slower                                                 |
| pickle_pure_python   | 300 us                                                 | 303 us: 1.01x slower                                                 |
| json_loads           | 27.0 us                                                | 27.3 us: 1.01x slower                                                |
| pickle_dict          | 33.2 us                                                | 33.8 us: 1.02x slower                                                |
| pickle_list          | 5.01 us                                                | 5.14 us: 1.03x slower                                                |
| unpickle_list        | 4.96 us                                                | 5.19 us: 1.05x slower                                                |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                |
| python_startup_no_site | 6.99 ms                                                | 7.07 ms: 1.01x slower                                                |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.84 ms: 1.13x faster                                                |
| django_template | 34.4 ms                                                | 36.0 ms: 1.05x slower                                                |
| genshi_text     | 22.9 ms                                                | 25.2 ms: 1.10x slower                                                |
| genshi_xml      | 50.3 ms                                                | 59.8 ms: 1.19x slower                                                |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240912-linux-x86_64-brandtbucher-deopt_tracing-3.14.0a0-282ab23 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 26.8 us: 1.42x faster                                                |
| deepcopy                   | 352 us                                                 | 259 us: 1.36x faster                                                 |
| async_tree_memoization_tg  | 465 ms                                                 | 385 ms: 1.21x faster                                                 |
| richards                   | 48.1 ms                                                | 39.9 ms: 1.21x faster                                                |
| deepcopy_reduce            | 3.17 us                                                | 2.66 us: 1.19x faster                                                |
| richards_super             | 54.4 ms                                                | 45.7 ms: 1.19x faster                                                |
| scimark_fft                | 369 ms                                                 | 310 ms: 1.19x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.36 ms: 1.15x faster                                                |
| spectral_norm              | 115 ms                                                 | 100 ms: 1.14x faster                                                 |
| mako                       | 11.1 ms                                                | 9.84 ms: 1.13x faster                                                |
| async_tree_memoization     | 442 ms                                                 | 392 ms: 1.13x faster                                                 |
| async_tree_none            | 354 ms                                                 | 314 ms: 1.13x faster                                                 |
| xml_etree_generate         | 87.0 ms                                                | 77.2 ms: 1.13x faster                                                |
| float                      | 78.5 ms                                                | 70.0 ms: 1.12x faster                                                |
| xml_etree_process          | 60.4 ms                                                | 54.2 ms: 1.11x faster                                                |
| crypto_pyaes               | 73.0 ms                                                | 67.0 ms: 1.09x faster                                                |
| mdp                        | 2.74 sec                                               | 2.53 sec: 1.09x faster                                               |
| tomli_loads                | 2.11 sec                                               | 1.97 sec: 1.07x faster                                               |
| go                         | 142 ms                                                 | 132 ms: 1.07x faster                                                 |
| telco                      | 8.45 ms                                                | 7.89 ms: 1.07x faster                                                |
| nbody                      | 85.7 ms                                                | 80.2 ms: 1.07x faster                                                |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                 |
| scimark_monte_carlo        | 66.3 ms                                                | 62.3 ms: 1.06x faster                                                |
| pathlib                    | 17.1 ms                                                | 16.1 ms: 1.06x faster                                                |
| bpe_tokeniser              | 4.69 sec                                               | 4.45 sec: 1.05x faster                                               |
| async_tree_none_tg         | 320 ms                                                 | 305 ms: 1.05x faster                                                 |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.05x faster                                                 |
| regex_effbot               | 3.88 ms                                                | 3.75 ms: 1.04x faster                                                |
| scimark_lu                 | 115 ms                                                 | 111 ms: 1.04x faster                                                 |
| xml_etree_iterparse        | 102 ms                                                 | 98.8 ms: 1.03x faster                                                |
| sqlite_synth               | 2.85 us                                                | 2.77 us: 1.03x faster                                                |
| fannkuch                   | 381 ms                                                 | 371 ms: 1.03x faster                                                 |
| thrift                     | 796 us                                                 | 778 us: 1.02x faster                                                 |
| unpickle                   | 14.9 us                                                | 14.5 us: 1.02x faster                                                |
| html5lib                   | 64.5 ms                                                | 63.3 ms: 1.02x faster                                                |
| pprint_safe_repr           | 744 ms                                                 | 730 ms: 1.02x faster                                                 |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                 |
| pyflate                    | 460 ms                                                 | 451 ms: 1.02x faster                                                 |
| json                       | 5.20 ms                                                | 5.12 ms: 1.02x faster                                                |
| logging_simple             | 5.66 us                                                | 5.60 us: 1.01x faster                                                |
| regex_v8                   | 25.3 ms                                                | 25.1 ms: 1.01x faster                                                |
| pickle                     | 11.6 us                                                | 11.5 us: 1.01x faster                                                |
| pidigits                   | 186 ms                                                 | 185 ms: 1.00x faster                                                 |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.00x faster                                                |
| gc_traversal               | 3.81 ms                                                | 3.83 ms: 1.01x slower                                                |
| unpickle_pure_python       | 213 us                                                 | 215 us: 1.01x slower                                                 |
| pycparser                  | 1.19 sec                                               | 1.20 sec: 1.01x slower                                               |
| coroutines                 | 22.5 ms                                                | 22.7 ms: 1.01x slower                                                |
| pickle_pure_python         | 300 us                                                 | 303 us: 1.01x slower                                                 |
| comprehensions             | 16.4 us                                                | 16.6 us: 1.01x slower                                                |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.81 sec: 1.01x slower                                               |
| json_loads                 | 27.0 us                                                | 27.3 us: 1.01x slower                                                |
| python_startup_no_site     | 6.99 ms                                                | 7.07 ms: 1.01x slower                                                |
| deltablue                  | 3.15 ms                                                | 3.19 ms: 1.01x slower                                                |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                 |
| asyncio_tcp                | 488 ms                                                 | 496 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 553 ms: 1.02x slower                                                 |
| pickle_dict                | 33.2 us                                                | 33.8 us: 1.02x slower                                                |
| typing_runtime_protocols   | 159 us                                                 | 162 us: 1.02x slower                                                 |
| regex_dna                  | 220 ms                                                 | 224 ms: 1.02x slower                                                 |
| bench_thread_pool          | 815 us                                                 | 835 us: 1.02x slower                                                 |
| pickle_list                | 5.01 us                                                | 5.14 us: 1.03x slower                                                |
| pprint_pformat             | 1.51 sec                                               | 1.56 sec: 1.03x slower                                               |
| tornado_http               | 91.5 ms                                                | 94.7 ms: 1.03x slower                                                |
| nqueens                    | 80.6 ms                                                | 83.5 ms: 1.04x slower                                                |
| 2to3                       | 265 ms                                                 | 275 ms: 1.04x slower                                                 |
| async_tree_io_tg           | 825 ms                                                 | 861 ms: 1.04x slower                                                 |
| django_template            | 34.4 ms                                                | 36.0 ms: 1.05x slower                                                |
| unpickle_list              | 4.96 us                                                | 5.19 us: 1.05x slower                                                |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.06x slower                                                |
| async_generators           | 433 ms                                                 | 458 ms: 1.06x slower                                                 |
| raytrace                   | 262 ms                                                 | 277 ms: 1.06x slower                                                 |
| sqlglot_normalize          | 107 ms                                                 | 115 ms: 1.07x slower                                                 |
| regex_compile              | 131 ms                                                 | 140 ms: 1.07x slower                                                 |
| sqlglot_transpile          | 1.57 ms                                                | 1.68 ms: 1.07x slower                                                |
| sqlglot_optimize           | 53.9 ms                                                | 57.8 ms: 1.07x slower                                                |
| dulwich_log                | 63.0 ms                                                | 67.7 ms: 1.08x slower                                                |
| sympy_str                  | 274 ms                                                 | 296 ms: 1.08x slower                                                 |
| sympy_expand               | 462 ms                                                 | 500 ms: 1.08x slower                                                 |
| create_gc_cycles           | 1.61 ms                                                | 1.76 ms: 1.09x slower                                                |
| genshi_text                | 22.9 ms                                                | 25.2 ms: 1.10x slower                                                |
| hexiom                     | 6.13 ms                                                | 6.87 ms: 1.12x slower                                                |
| docutils                   | 2.58 sec                                               | 2.94 sec: 1.14x slower                                               |
| sympy_integrate            | 19.9 ms                                                | 22.7 ms: 1.14x slower                                                |
| sympy_sum                  | 150 ms                                                 | 171 ms: 1.14x slower                                                 |
| generators                 | 28.8 ms                                                | 33.1 ms: 1.15x slower                                                |
| genshi_xml                 | 50.3 ms                                                | 59.8 ms: 1.19x slower                                                |
| pylint                     | 313 ms                                                 | 374 ms: 1.19x slower                                                 |
| unpack_sequence            | 42.4 ns                                                | 108 ns: 2.55x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, logging_format, asyncio_websockets, chaos, bench_mp_pool, coverage, async_tree_io
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 76.09% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x