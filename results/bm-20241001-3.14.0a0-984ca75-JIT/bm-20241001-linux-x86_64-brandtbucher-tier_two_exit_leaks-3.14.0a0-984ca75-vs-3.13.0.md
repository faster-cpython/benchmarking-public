# Results vs. 3.13.0

- fork: brandtbucher
- ref: tier_two_exit_leaks
- machine: linux-x86_64
- commit hash: 984ca75
- commit date: 2024-10-01
- overall geometric mean: 1.01x slower
- HPT reliability: 50.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 279 ms: 1.05x slower                                                       |
| docutils       | 2.58 sec                                               | 2.92 sec: 1.13x slower                                                     |
| html5lib       | 64.5 ms                                                | 66.2 ms: 1.03x slower                                                      |
| tornado_http   | 91.5 ms                                                | 95.7 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                  | 1.06x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 391 ms: 1.19x faster                                                       |
| async_tree_none            | 354 ms                                                 | 321 ms: 1.10x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 410 ms: 1.08x faster                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                     |
| asyncio_tcp                | 488 ms                                                 | 494 ms: 1.01x slower                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 554 ms: 1.02x slower                                                       |
| coroutines                 | 22.5 ms                                                | 23.3 ms: 1.03x slower                                                      |
| async_generators           | 433 ms                                                 | 457 ms: 1.05x slower                                                       |
| async_tree_io              | 843 ms                                                 | 891 ms: 1.06x slower                                                       |
| async_tree_io_tg           | 825 ms                                                 | 880 ms: 1.07x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (3): async_tree_none_tg, asyncio_websockets, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 72.3 ms: 1.09x faster                                                      |
| nbody          | 85.7 ms                                                | 80.5 ms: 1.07x faster                                                      |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.65 ms: 1.07x faster                                                      |
| regex_v8       | 25.3 ms                                                | 24.3 ms: 1.04x faster                                                      |
| regex_dna      | 220 ms                                                 | 222 ms: 1.01x slower                                                       |
| regex_compile  | 131 ms                                                 | 143 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                  | 1.00x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|---------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_generate  | 87.0 ms                                                | 77.7 ms: 1.12x faster                                                      |
| tomli_loads         | 2.11 sec                                               | 1.93 sec: 1.10x faster                                                     |
| xml_etree_process   | 60.4 ms                                                | 55.2 ms: 1.09x faster                                                      |
| xml_etree_parse     | 156 ms                                                 | 145 ms: 1.07x faster                                                       |
| xml_etree_iterparse | 102 ms                                                 | 97.5 ms: 1.05x faster                                                      |
| unpickle            | 14.9 us                                                | 14.7 us: 1.01x faster                                                      |
| json_loads          | 27.0 us                                                | 26.7 us: 1.01x faster                                                      |
| json_dumps          | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                      |
| pickle              | 11.6 us                                                | 11.7 us: 1.01x slower                                                      |
| pickle_pure_python  | 300 us                                                 | 310 us: 1.03x slower                                                       |
| pickle_list         | 5.01 us                                                | 5.18 us: 1.03x slower                                                      |
| pickle_dict         | 33.2 us                                                | 34.7 us: 1.05x slower                                                      |
| unpickle_list       | 4.96 us                                                | 5.33 us: 1.07x slower                                                      |
| Geometric mean      | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                      |
| python_startup_no_site | 6.99 ms                                                | 7.06 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.87 ms: 1.13x faster                                                      |
| django_template | 34.4 ms                                                | 36.0 ms: 1.05x slower                                                      |
| genshi_text     | 22.9 ms                                                | 25.3 ms: 1.11x slower                                                      |
| genshi_xml      | 50.3 ms                                                | 59.2 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-linux-x86_64-brandtbucher-tier_two_exit_leaks-3.14.0a0-984ca75 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 27.0 us: 1.41x faster                                                      |
| deepcopy                   | 352 us                                                 | 271 us: 1.30x faster                                                       |
| richards_super             | 54.4 ms                                                | 45.1 ms: 1.21x faster                                                      |
| richards                   | 48.1 ms                                                | 40.0 ms: 1.20x faster                                                      |
| scimark_fft                | 369 ms                                                 | 307 ms: 1.20x faster                                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 391 ms: 1.19x faster                                                       |
| deepcopy_reduce            | 3.17 us                                                | 2.67 us: 1.19x faster                                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.37 ms: 1.15x faster                                                      |
| telco                      | 8.45 ms                                                | 7.49 ms: 1.13x faster                                                      |
| mako                       | 11.1 ms                                                | 9.87 ms: 1.13x faster                                                      |
| xml_etree_generate         | 87.0 ms                                                | 77.7 ms: 1.12x faster                                                      |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                       |
| crypto_pyaes               | 73.0 ms                                                | 65.7 ms: 1.11x faster                                                      |
| async_tree_none            | 354 ms                                                 | 321 ms: 1.10x faster                                                       |
| tomli_loads                | 2.11 sec                                               | 1.93 sec: 1.10x faster                                                     |
| xml_etree_process          | 60.4 ms                                                | 55.2 ms: 1.09x faster                                                      |
| pathlib                    | 17.1 ms                                                | 15.7 ms: 1.09x faster                                                      |
| float                      | 78.5 ms                                                | 72.3 ms: 1.09x faster                                                      |
| mdp                        | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                     |
| async_tree_memoization     | 442 ms                                                 | 410 ms: 1.08x faster                                                       |
| go                         | 142 ms                                                 | 132 ms: 1.07x faster                                                       |
| xml_etree_parse            | 156 ms                                                 | 145 ms: 1.07x faster                                                       |
| nbody                      | 85.7 ms                                                | 80.5 ms: 1.07x faster                                                      |
| regex_effbot               | 3.88 ms                                                | 3.65 ms: 1.07x faster                                                      |
| bpe_tokeniser              | 4.69 sec                                               | 4.42 sec: 1.06x faster                                                     |
| scimark_monte_carlo        | 66.3 ms                                                | 62.5 ms: 1.06x faster                                                      |
| scimark_lu                 | 115 ms                                                 | 109 ms: 1.05x faster                                                       |
| xml_etree_iterparse        | 102 ms                                                 | 97.5 ms: 1.05x faster                                                      |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.05x faster                                                       |
| sqlite_synth               | 2.85 us                                                | 2.74 us: 1.04x faster                                                      |
| regex_v8                   | 25.3 ms                                                | 24.3 ms: 1.04x faster                                                      |
| json                       | 5.20 ms                                                | 5.02 ms: 1.04x faster                                                      |
| logging_format             | 6.25 us                                                | 6.08 us: 1.03x faster                                                      |
| pycparser                  | 1.19 sec                                               | 1.16 sec: 1.03x faster                                                     |
| logging_simple             | 5.66 us                                                | 5.54 us: 1.02x faster                                                      |
| pprint_safe_repr           | 744 ms                                                 | 735 ms: 1.01x faster                                                       |
| fannkuch                   | 381 ms                                                 | 376 ms: 1.01x faster                                                       |
| unpickle                   | 14.9 us                                                | 14.7 us: 1.01x faster                                                      |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.01x faster                                                       |
| json_loads                 | 27.0 us                                                | 26.7 us: 1.01x faster                                                      |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                                      |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                       |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                     |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                                      |
| regex_dna                  | 220 ms                                                 | 222 ms: 1.01x slower                                                       |
| python_startup_no_site     | 6.99 ms                                                | 7.06 ms: 1.01x slower                                                      |
| asyncio_tcp                | 488 ms                                                 | 494 ms: 1.01x slower                                                       |
| thrift                     | 796 us                                                 | 809 us: 1.02x slower                                                       |
| deltablue                  | 3.15 ms                                                | 3.21 ms: 1.02x slower                                                      |
| coverage                   | 83.7 ms                                                | 85.3 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 554 ms: 1.02x slower                                                       |
| pprint_pformat             | 1.51 sec                                               | 1.54 sec: 1.02x slower                                                     |
| comprehensions             | 16.4 us                                                | 16.8 us: 1.02x slower                                                      |
| html5lib                   | 64.5 ms                                                | 66.2 ms: 1.03x slower                                                      |
| chaos                      | 58.4 ms                                                | 60.0 ms: 1.03x slower                                                      |
| logging_silent             | 102 ns                                                 | 105 ns: 1.03x slower                                                       |
| pickle_pure_python         | 300 us                                                 | 310 us: 1.03x slower                                                       |
| pickle_list                | 5.01 us                                                | 5.18 us: 1.03x slower                                                      |
| coroutines                 | 22.5 ms                                                | 23.3 ms: 1.03x slower                                                      |
| typing_runtime_protocols   | 159 us                                                 | 165 us: 1.04x slower                                                       |
| tornado_http               | 91.5 ms                                                | 95.7 ms: 1.05x slower                                                      |
| pickle_dict                | 33.2 us                                                | 34.7 us: 1.05x slower                                                      |
| django_template            | 34.4 ms                                                | 36.0 ms: 1.05x slower                                                      |
| gc_traversal               | 3.81 ms                                                | 3.99 ms: 1.05x slower                                                      |
| 2to3                       | 265 ms                                                 | 279 ms: 1.05x slower                                                       |
| async_generators           | 433 ms                                                 | 457 ms: 1.05x slower                                                       |
| raytrace                   | 262 ms                                                 | 276 ms: 1.06x slower                                                       |
| async_tree_io              | 843 ms                                                 | 891 ms: 1.06x slower                                                       |
| async_tree_io_tg           | 825 ms                                                 | 880 ms: 1.07x slower                                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.35 ms: 1.07x slower                                                      |
| create_gc_cycles           | 1.61 ms                                                | 1.73 ms: 1.07x slower                                                      |
| unpickle_list              | 4.96 us                                                | 5.33 us: 1.07x slower                                                      |
| dulwich_log                | 63.0 ms                                                | 67.8 ms: 1.08x slower                                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.70 ms: 1.08x slower                                                      |
| sqlglot_normalize          | 107 ms                                                 | 117 ms: 1.09x slower                                                       |
| regex_compile              | 131 ms                                                 | 143 ms: 1.09x slower                                                       |
| bench_thread_pool          | 815 us                                                 | 894 us: 1.10x slower                                                       |
| nqueens                    | 80.6 ms                                                | 88.6 ms: 1.10x slower                                                      |
| sympy_expand               | 462 ms                                                 | 508 ms: 1.10x slower                                                       |
| genshi_text                | 22.9 ms                                                | 25.3 ms: 1.11x slower                                                      |
| sympy_str                  | 274 ms                                                 | 305 ms: 1.11x slower                                                       |
| sqlglot_optimize           | 53.9 ms                                                | 60.5 ms: 1.12x slower                                                      |
| hexiom                     | 6.13 ms                                                | 6.92 ms: 1.13x slower                                                      |
| docutils                   | 2.58 sec                                               | 2.92 sec: 1.13x slower                                                     |
| genshi_xml                 | 50.3 ms                                                | 59.2 ms: 1.18x slower                                                      |
| sympy_sum                  | 150 ms                                                 | 176 ms: 1.18x slower                                                       |
| sympy_integrate            | 19.9 ms                                                | 23.5 ms: 1.18x slower                                                      |
| pylint                     | 313 ms                                                 | 374 ms: 1.20x slower                                                       |
| generators                 | 28.8 ms                                                | 34.9 ms: 1.21x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 60.7 ms: 2.53x slower                                                      |
| unpack_sequence            | 42.4 ns                                                | 108 ns: 2.55x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (5): async_tree_none_tg, unpickle_pure_python, asyncio_websockets, async_tree_cpu_io_mixed, pyflate
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 50.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.06x