# Results vs. 3.13.0

- fork: brandtbucher
- ref: ujb0_project_warmup
- machine: linux-x86_64
- commit hash: f67fedc
- commit date: 2024-09-09
- overall geometric mean: 1.05x slower
- HPT reliability: 98.83%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 292 ms: 1.10x slower                                                       |
| docutils       | 2.58 sec                                               | 3.47 sec: 1.34x slower                                                     |
| html5lib       | 64.5 ms                                                | 70.6 ms: 1.09x slower                                                      |
| tornado_http   | 91.5 ms                                                | 119 ms: 1.30x slower                                                       |
| Geometric mean | (ref)                                                  | 1.21x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 409 ms: 1.14x faster                                                       |
| async_tree_memoization    | 442 ms                                                 | 422 ms: 1.05x faster                                                       |
| async_tree_none           | 354 ms                                                 | 339 ms: 1.04x faster                                                       |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.82 sec: 1.02x slower                                                     |
| async_generators          | 433 ms                                                 | 455 ms: 1.05x slower                                                       |
| coroutines                | 22.5 ms                                                | 23.9 ms: 1.06x slower                                                      |
| asyncio_tcp               | 488 ms                                                 | 522 ms: 1.07x slower                                                       |
| async_tree_io_tg          | 825 ms                                                 | 919 ms: 1.11x slower                                                       |
| async_tree_io             | 843 ms                                                 | 947 ms: 1.12x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.02x slower                                                               |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 69.9 ms: 1.12x faster                                                      |
| nbody          | 85.7 ms                                                | 82.2 ms: 1.04x faster                                                      |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.77 ms: 1.03x faster                                                      |
| regex_dna      | 220 ms                                                 | 215 ms: 1.02x faster                                                       |
| regex_v8       | 25.3 ms                                                | 25.9 ms: 1.03x slower                                                      |
| regex_compile  | 131 ms                                                 | 155 ms: 1.18x slower                                                       |
| Geometric mean | (ref)                                                  | 1.04x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 54.0 ms: 1.12x faster                                                      |
| unpickle_pure_python | 213 us                                                 | 191 us: 1.12x faster                                                       |
| xml_etree_generate   | 87.0 ms                                                | 78.1 ms: 1.11x faster                                                      |
| xml_etree_parse      | 156 ms                                                 | 144 ms: 1.08x faster                                                       |
| json_dumps           | 10.4 ms                                                | 9.90 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 102 ms                                                 | 98.2 ms: 1.04x faster                                                      |
| tomli_loads          | 2.11 sec                                               | 2.06 sec: 1.03x faster                                                     |
| pickle               | 11.6 us                                                | 11.4 us: 1.02x faster                                                      |
| unpickle             | 14.9 us                                                | 14.7 us: 1.01x faster                                                      |
| pickle_list          | 5.01 us                                                | 5.19 us: 1.04x slower                                                      |
| pickle_pure_python   | 300 us                                                 | 314 us: 1.05x slower                                                       |
| pickle_dict          | 33.2 us                                                | 35.2 us: 1.06x slower                                                      |
| unpickle_list        | 4.96 us                                                | 5.31 us: 1.07x slower                                                      |
| json_loads           | 27.0 us                                                | 29.5 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.8 ms: 1.02x slower                                                      |
| python_startup_no_site | 6.99 ms                                                | 7.19 ms: 1.03x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.65 ms: 1.15x faster                                                      |
| genshi_text     | 22.9 ms                                                | 22.6 ms: 1.01x faster                                                      |
| django_template | 34.4 ms                                                | 38.8 ms: 1.13x slower                                                      |
| genshi_xml      | 50.3 ms                                                | 59.0 ms: 1.17x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                               |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240909-linux-x86_64-brandtbucher-ujb0_project_warmup-3.14.0a0-f67fedc |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 27.1 us: 1.40x faster                                                      |
| deepcopy                  | 352 us                                                 | 267 us: 1.32x faster                                                       |
| scimark_fft               | 369 ms                                                 | 312 ms: 1.18x faster                                                       |
| mako                      | 11.1 ms                                                | 9.65 ms: 1.15x faster                                                      |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.38 ms: 1.15x faster                                                      |
| scimark_monte_carlo       | 66.3 ms                                                | 58.1 ms: 1.14x faster                                                      |
| deepcopy_reduce           | 3.17 us                                                | 2.79 us: 1.14x faster                                                      |
| async_tree_memoization_tg | 465 ms                                                 | 409 ms: 1.14x faster                                                       |
| float                     | 78.5 ms                                                | 69.9 ms: 1.12x faster                                                      |
| xml_etree_process         | 60.4 ms                                                | 54.0 ms: 1.12x faster                                                      |
| unpickle_pure_python      | 213 us                                                 | 191 us: 1.12x faster                                                       |
| xml_etree_generate        | 87.0 ms                                                | 78.1 ms: 1.11x faster                                                      |
| telco                     | 8.45 ms                                                | 7.75 ms: 1.09x faster                                                      |
| xml_etree_parse           | 156 ms                                                 | 144 ms: 1.08x faster                                                       |
| pathlib                   | 17.1 ms                                                | 15.9 ms: 1.07x faster                                                      |
| spectral_norm             | 115 ms                                                 | 107 ms: 1.07x faster                                                       |
| crypto_pyaes              | 73.0 ms                                                | 68.2 ms: 1.07x faster                                                      |
| scimark_lu                | 115 ms                                                 | 109 ms: 1.05x faster                                                       |
| json_dumps                | 10.4 ms                                                | 9.90 ms: 1.05x faster                                                      |
| async_tree_memoization    | 442 ms                                                 | 422 ms: 1.05x faster                                                       |
| async_tree_none           | 354 ms                                                 | 339 ms: 1.04x faster                                                       |
| nbody                     | 85.7 ms                                                | 82.2 ms: 1.04x faster                                                      |
| bpe_tokeniser             | 4.69 sec                                               | 4.51 sec: 1.04x faster                                                     |
| xml_etree_iterparse       | 102 ms                                                 | 98.2 ms: 1.04x faster                                                      |
| regex_effbot              | 3.88 ms                                                | 3.77 ms: 1.03x faster                                                      |
| sqlite_synth              | 2.85 us                                                | 2.77 us: 1.03x faster                                                      |
| tomli_loads               | 2.11 sec                                               | 2.06 sec: 1.03x faster                                                     |
| fannkuch                  | 381 ms                                                 | 372 ms: 1.02x faster                                                       |
| regex_dna                 | 220 ms                                                 | 215 ms: 1.02x faster                                                       |
| pickle                    | 11.6 us                                                | 11.4 us: 1.02x faster                                                      |
| unpickle                  | 14.9 us                                                | 14.7 us: 1.01x faster                                                      |
| genshi_text               | 22.9 ms                                                | 22.6 ms: 1.01x faster                                                      |
| mdp                       | 2.74 sec                                               | 2.72 sec: 1.01x faster                                                     |
| scimark_sor               | 122 ms                                                 | 122 ms: 1.01x faster                                                       |
| gc_traversal              | 3.81 ms                                                | 3.78 ms: 1.01x faster                                                      |
| pidigits                  | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| meteor_contest            | 108 ms                                                 | 108 ms: 1.01x slower                                                       |
| logging_silent            | 102 ns                                                 | 103 ns: 1.01x slower                                                       |
| thrift                    | 796 us                                                 | 809 us: 1.02x slower                                                       |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.82 sec: 1.02x slower                                                     |
| json                      | 5.20 ms                                                | 5.29 ms: 1.02x slower                                                      |
| python_startup            | 10.6 ms                                                | 10.8 ms: 1.02x slower                                                      |
| coverage                  | 83.7 ms                                                | 85.4 ms: 1.02x slower                                                      |
| pprint_safe_repr          | 744 ms                                                 | 761 ms: 1.02x slower                                                       |
| pyflate                   | 460 ms                                                 | 471 ms: 1.03x slower                                                       |
| regex_v8                  | 25.3 ms                                                | 25.9 ms: 1.03x slower                                                      |
| logging_format            | 6.25 us                                                | 6.43 us: 1.03x slower                                                      |
| python_startup_no_site    | 6.99 ms                                                | 7.19 ms: 1.03x slower                                                      |
| typing_runtime_protocols  | 159 us                                                 | 164 us: 1.03x slower                                                       |
| comprehensions            | 16.4 us                                                | 17.0 us: 1.04x slower                                                      |
| pickle_list               | 5.01 us                                                | 5.19 us: 1.04x slower                                                      |
| logging_simple            | 5.66 us                                                | 5.88 us: 1.04x slower                                                      |
| nqueens                   | 80.6 ms                                                | 84.0 ms: 1.04x slower                                                      |
| deltablue                 | 3.15 ms                                                | 3.29 ms: 1.04x slower                                                      |
| pickle_pure_python        | 300 us                                                 | 314 us: 1.05x slower                                                       |
| async_generators          | 433 ms                                                 | 455 ms: 1.05x slower                                                       |
| raytrace                  | 262 ms                                                 | 275 ms: 1.05x slower                                                       |
| pickle_dict               | 33.2 us                                                | 35.2 us: 1.06x slower                                                      |
| coroutines                | 22.5 ms                                                | 23.9 ms: 1.06x slower                                                      |
| chaos                     | 58.4 ms                                                | 62.3 ms: 1.07x slower                                                      |
| asyncio_tcp               | 488 ms                                                 | 522 ms: 1.07x slower                                                       |
| unpickle_list             | 4.96 us                                                | 5.31 us: 1.07x slower                                                      |
| pycparser                 | 1.19 sec                                               | 1.30 sec: 1.09x slower                                                     |
| html5lib                  | 64.5 ms                                                | 70.6 ms: 1.09x slower                                                      |
| json_loads                | 27.0 us                                                | 29.5 us: 1.09x slower                                                      |
| pprint_pformat            | 1.51 sec                                               | 1.66 sec: 1.10x slower                                                     |
| 2to3                      | 265 ms                                                 | 292 ms: 1.10x slower                                                       |
| bench_thread_pool         | 815 us                                                 | 898 us: 1.10x slower                                                       |
| create_gc_cycles          | 1.61 ms                                                | 1.79 ms: 1.11x slower                                                      |
| async_tree_io_tg          | 825 ms                                                 | 919 ms: 1.11x slower                                                       |
| richards                  | 48.1 ms                                                | 53.8 ms: 1.12x slower                                                      |
| richards_super            | 54.4 ms                                                | 60.8 ms: 1.12x slower                                                      |
| async_tree_io             | 843 ms                                                 | 947 ms: 1.12x slower                                                       |
| django_template           | 34.4 ms                                                | 38.8 ms: 1.13x slower                                                      |
| sqlglot_normalize         | 107 ms                                                 | 125 ms: 1.16x slower                                                       |
| hexiom                    | 6.13 ms                                                | 7.14 ms: 1.17x slower                                                      |
| genshi_xml                | 50.3 ms                                                | 59.0 ms: 1.17x slower                                                      |
| regex_compile             | 131 ms                                                 | 155 ms: 1.18x slower                                                       |
| sympy_expand              | 462 ms                                                 | 556 ms: 1.20x slower                                                       |
| generators                | 28.8 ms                                                | 34.8 ms: 1.21x slower                                                      |
| sqlglot_optimize          | 53.9 ms                                                | 67.1 ms: 1.24x slower                                                      |
| sympy_str                 | 274 ms                                                 | 341 ms: 1.25x slower                                                       |
| go                        | 142 ms                                                 | 178 ms: 1.26x slower                                                       |
| tornado_http              | 91.5 ms                                                | 119 ms: 1.30x slower                                                       |
| docutils                  | 2.58 sec                                               | 3.47 sec: 1.34x slower                                                     |
| sqlglot_parse             | 1.27 ms                                                | 1.73 ms: 1.36x slower                                                      |
| sympy_integrate           | 19.9 ms                                                | 27.3 ms: 1.37x slower                                                      |
| sqlglot_transpile         | 1.57 ms                                                | 2.17 ms: 1.38x slower                                                      |
| sympy_sum                 | 150 ms                                                 | 214 ms: 1.43x slower                                                       |
| pylint                    | 313 ms                                                 | 480 ms: 1.53x slower                                                       |
| unpack_sequence           | 42.4 ns                                                | 148 ns: 3.50x slower                                                       |
| Geometric mean            | (ref)                                                  | 1.05x slower                                                               |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_cpu_io_mixed, bench_mp_pool, asyncio_websockets, async_tree_cpu_io_mixed_tg
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, dulwich_log, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 98.83% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.17x