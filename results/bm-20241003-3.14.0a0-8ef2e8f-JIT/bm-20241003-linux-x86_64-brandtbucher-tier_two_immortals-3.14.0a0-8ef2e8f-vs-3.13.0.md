# Results vs. 3.13.0

- fork: brandtbucher
- ref: tier_two_immortals
- machine: linux-x86_64
- commit hash: 8ef2e8f
- commit date: 2024-10-03
- overall geometric mean: 1.01x slower
- HPT reliability: 58.82%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 279 ms: 1.05x slower                                                      |
| docutils       | 2.58 sec                                               | 2.92 sec: 1.13x slower                                                    |
| tornado_http   | 91.5 ms                                                | 94.9 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                  | 1.05x slower                                                              |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg | 465 ms                                                 | 387 ms: 1.20x faster                                                      |
| async_tree_none           | 354 ms                                                 | 317 ms: 1.12x faster                                                      |
| async_tree_memoization    | 442 ms                                                 | 408 ms: 1.09x faster                                                      |
| async_tree_none_tg        | 320 ms                                                 | 307 ms: 1.04x faster                                                      |
| asyncio_tcp               | 488 ms                                                 | 484 ms: 1.01x faster                                                      |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                    |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                      |
| async_generators          | 433 ms                                                 | 452 ms: 1.04x slower                                                      |
| async_tree_io             | 843 ms                                                 | 885 ms: 1.05x slower                                                      |
| async_tree_io_tg          | 825 ms                                                 | 872 ms: 1.06x slower                                                      |
| Geometric mean            | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, coroutines, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 71.8 ms: 1.09x faster                                                     |
| nbody          | 85.7 ms                                                | 82.3 ms: 1.04x faster                                                     |
| pidigits       | 186 ms                                                 | 185 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.69 ms: 1.05x faster                                                     |
| regex_dna      | 220 ms                                                 | 221 ms: 1.01x slower                                                      |
| regex_v8       | 25.3 ms                                                | 25.5 ms: 1.01x slower                                                     |
| regex_compile  | 131 ms                                                 | 143 ms: 1.09x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate  | 87.0 ms                                                | 76.8 ms: 1.13x faster                                                     |
| tomli_loads         | 2.11 sec                                               | 1.90 sec: 1.11x faster                                                    |
| xml_etree_process   | 60.4 ms                                                | 54.4 ms: 1.11x faster                                                     |
| xml_etree_parse     | 156 ms                                                 | 145 ms: 1.08x faster                                                      |
| xml_etree_iterparse | 102 ms                                                 | 98.1 ms: 1.04x faster                                                     |
| json_dumps          | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                     |
| pickle_list         | 5.01 us                                                | 4.91 us: 1.02x faster                                                     |
| pickle              | 11.6 us                                                | 11.4 us: 1.02x faster                                                     |
| json_loads          | 27.0 us                                                | 26.9 us: 1.00x faster                                                     |
| pickle_pure_python  | 300 us                                                 | 309 us: 1.03x slower                                                      |
| pickle_dict         | 33.2 us                                                | 34.4 us: 1.04x slower                                                     |
| unpickle_list       | 4.96 us                                                | 5.16 us: 1.04x slower                                                     |
| Geometric mean      | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (2): unpickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                     |
| python_startup_no_site | 6.99 ms                                                | 7.03 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.90 ms: 1.12x faster                                                     |
| django_template | 34.4 ms                                                | 36.9 ms: 1.07x slower                                                     |
| genshi_text     | 22.9 ms                                                | 25.5 ms: 1.12x slower                                                     |
| genshi_xml      | 50.3 ms                                                | 57.9 ms: 1.15x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                              |

All benchmarks:
===============

| Benchmark                 | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|---------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo             | 38.0 us                                                | 27.1 us: 1.40x faster                                                     |
| deepcopy                  | 352 us                                                 | 271 us: 1.30x faster                                                      |
| richards                  | 48.1 ms                                                | 39.5 ms: 1.22x faster                                                     |
| richards_super            | 54.4 ms                                                | 44.7 ms: 1.22x faster                                                     |
| async_tree_memoization_tg | 465 ms                                                 | 387 ms: 1.20x faster                                                      |
| scimark_fft               | 369 ms                                                 | 307 ms: 1.20x faster                                                      |
| deepcopy_reduce           | 3.17 us                                                | 2.65 us: 1.20x faster                                                     |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 4.36 ms: 1.15x faster                                                     |
| spectral_norm             | 115 ms                                                 | 100 ms: 1.15x faster                                                      |
| xml_etree_generate        | 87.0 ms                                                | 76.8 ms: 1.13x faster                                                     |
| telco                     | 8.45 ms                                                | 7.49 ms: 1.13x faster                                                     |
| mako                      | 11.1 ms                                                | 9.90 ms: 1.12x faster                                                     |
| async_tree_none           | 354 ms                                                 | 317 ms: 1.12x faster                                                      |
| crypto_pyaes              | 73.0 ms                                                | 65.4 ms: 1.12x faster                                                     |
| tomli_loads               | 2.11 sec                                               | 1.90 sec: 1.11x faster                                                    |
| xml_etree_process         | 60.4 ms                                                | 54.4 ms: 1.11x faster                                                     |
| pathlib                   | 17.1 ms                                                | 15.6 ms: 1.09x faster                                                     |
| float                     | 78.5 ms                                                | 71.8 ms: 1.09x faster                                                     |
| async_tree_memoization    | 442 ms                                                 | 408 ms: 1.09x faster                                                      |
| mdp                       | 2.74 sec                                               | 2.54 sec: 1.08x faster                                                    |
| xml_etree_parse           | 156 ms                                                 | 145 ms: 1.08x faster                                                      |
| go                        | 142 ms                                                 | 132 ms: 1.07x faster                                                      |
| scimark_monte_carlo       | 66.3 ms                                                | 62.5 ms: 1.06x faster                                                     |
| bpe_tokeniser             | 4.69 sec                                               | 4.43 sec: 1.06x faster                                                    |
| pyflate                   | 460 ms                                                 | 435 ms: 1.06x faster                                                      |
| regex_effbot              | 3.88 ms                                                | 3.69 ms: 1.05x faster                                                     |
| async_tree_none_tg        | 320 ms                                                 | 307 ms: 1.04x faster                                                      |
| nbody                     | 85.7 ms                                                | 82.3 ms: 1.04x faster                                                     |
| scimark_lu                | 115 ms                                                 | 110 ms: 1.04x faster                                                      |
| scimark_sor               | 122 ms                                                 | 118 ms: 1.04x faster                                                      |
| xml_etree_iterparse       | 102 ms                                                 | 98.1 ms: 1.04x faster                                                     |
| sqlite_synth              | 2.85 us                                                | 2.76 us: 1.03x faster                                                     |
| json                      | 5.20 ms                                                | 5.06 ms: 1.03x faster                                                     |
| json_dumps                | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                     |
| fannkuch                  | 381 ms                                                 | 372 ms: 1.02x faster                                                      |
| pickle_list               | 5.01 us                                                | 4.91 us: 1.02x faster                                                     |
| pickle                    | 11.6 us                                                | 11.4 us: 1.02x faster                                                     |
| python_startup            | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                     |
| asyncio_tcp               | 488 ms                                                 | 484 ms: 1.01x faster                                                      |
| meteor_contest            | 108 ms                                                 | 107 ms: 1.01x faster                                                      |
| pidigits                  | 186 ms                                                 | 185 ms: 1.00x faster                                                      |
| json_loads                | 27.0 us                                                | 26.9 us: 1.00x faster                                                     |
| asyncio_tcp_ssl           | 1.79 sec                                               | 1.79 sec: 1.00x slower                                                    |
| asyncio_websockets        | 555 ms                                                 | 558 ms: 1.00x slower                                                      |
| regex_dna                 | 220 ms                                                 | 221 ms: 1.01x slower                                                      |
| python_startup_no_site    | 6.99 ms                                                | 7.03 ms: 1.01x slower                                                     |
| regex_v8                  | 25.3 ms                                                | 25.5 ms: 1.01x slower                                                     |
| gc_traversal              | 3.81 ms                                                | 3.85 ms: 1.01x slower                                                     |
| deltablue                 | 3.15 ms                                                | 3.19 ms: 1.01x slower                                                     |
| logging_silent            | 102 ns                                                 | 104 ns: 1.02x slower                                                      |
| chaos                     | 58.4 ms                                                | 59.7 ms: 1.02x slower                                                     |
| comprehensions            | 16.4 us                                                | 16.8 us: 1.02x slower                                                     |
| coverage                  | 83.7 ms                                                | 85.8 ms: 1.02x slower                                                     |
| pprint_pformat            | 1.51 sec                                               | 1.55 sec: 1.02x slower                                                    |
| pickle_pure_python        | 300 us                                                 | 309 us: 1.03x slower                                                      |
| tornado_http              | 91.5 ms                                                | 94.9 ms: 1.04x slower                                                     |
| pickle_dict               | 33.2 us                                                | 34.4 us: 1.04x slower                                                     |
| unpickle_list             | 4.96 us                                                | 5.16 us: 1.04x slower                                                     |
| typing_runtime_protocols  | 159 us                                                 | 166 us: 1.04x slower                                                      |
| async_generators          | 433 ms                                                 | 452 ms: 1.04x slower                                                      |
| async_tree_io             | 843 ms                                                 | 885 ms: 1.05x slower                                                      |
| 2to3                      | 265 ms                                                 | 279 ms: 1.05x slower                                                      |
| async_tree_io_tg          | 825 ms                                                 | 872 ms: 1.06x slower                                                      |
| raytrace                  | 262 ms                                                 | 278 ms: 1.06x slower                                                      |
| sqlglot_parse             | 1.27 ms                                                | 1.35 ms: 1.07x slower                                                     |
| nqueens                   | 80.6 ms                                                | 85.9 ms: 1.07x slower                                                     |
| sqlglot_normalize         | 107 ms                                                 | 114 ms: 1.07x slower                                                      |
| sqlglot_transpile         | 1.57 ms                                                | 1.68 ms: 1.07x slower                                                     |
| django_template           | 34.4 ms                                                | 36.9 ms: 1.07x slower                                                     |
| create_gc_cycles          | 1.61 ms                                                | 1.73 ms: 1.08x slower                                                     |
| dulwich_log               | 63.0 ms                                                | 68.2 ms: 1.08x slower                                                     |
| regex_compile             | 131 ms                                                 | 143 ms: 1.09x slower                                                      |
| sympy_expand              | 462 ms                                                 | 505 ms: 1.09x slower                                                      |
| bench_thread_pool         | 815 us                                                 | 896 us: 1.10x slower                                                      |
| sympy_str                 | 274 ms                                                 | 303 ms: 1.11x slower                                                      |
| genshi_text               | 22.9 ms                                                | 25.5 ms: 1.12x slower                                                     |
| sqlglot_optimize          | 53.9 ms                                                | 60.3 ms: 1.12x slower                                                     |
| docutils                  | 2.58 sec                                               | 2.92 sec: 1.13x slower                                                    |
| hexiom                    | 6.13 ms                                                | 6.95 ms: 1.13x slower                                                     |
| genshi_xml                | 50.3 ms                                                | 57.9 ms: 1.15x slower                                                     |
| sympy_sum                 | 150 ms                                                 | 175 ms: 1.17x slower                                                      |
| sympy_integrate           | 19.9 ms                                                | 23.4 ms: 1.18x slower                                                     |
| pylint                    | 313 ms                                                 | 374 ms: 1.20x slower                                                      |
| generators                | 28.8 ms                                                | 34.5 ms: 1.20x slower                                                     |
| bench_mp_pool             | 24.0 ms                                                | 60.2 ms: 2.51x slower                                                     |
| unpack_sequence           | 42.4 ns                                                | 108 ns: 2.56x slower                                                      |
| Geometric mean            | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed, pprint_safe_repr, coroutines, unpickle_pure_python, thrift, logging_simple, html5lib, logging_format, async_tree_cpu_io_mixed_tg, pycparser, unpickle
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 58.82% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x