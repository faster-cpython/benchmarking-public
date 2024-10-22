# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_likely
- machine: linux-x86_64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.04x slower
- HPT reliability: 86.47%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 278 ms: 1.05x slower                                                  |
| docutils       | 2.58 sec                                               | 2.92 sec: 1.13x slower                                                |
| html5lib       | 64.5 ms                                                | 64.0 ms: 1.01x faster                                                 |
| tornado_http   | 91.5 ms                                                | 95.0 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 375 ms: 1.24x faster                                                  |
| async_tree_none            | 354 ms                                                 | 329 ms: 1.08x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 420 ms: 1.05x faster                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                 |
| asyncio_tcp                | 488 ms                                                 | 499 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 556 ms: 1.02x slower                                                  |
| async_generators           | 433 ms                                                 | 454 ms: 1.05x slower                                                  |
| async_tree_io_tg           | 825 ms                                                 | 971 ms: 1.18x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, asyncio_websockets, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 76.0 ms: 1.03x faster                                                 |
| nbody          | 85.7 ms                                                | 84.5 ms: 1.02x faster                                                 |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.68 ms: 1.06x faster                                                 |
| regex_v8       | 25.3 ms                                                | 24.7 ms: 1.02x faster                                                 |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                                  |
| regex_compile  | 131 ms                                                 | 143 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 78.8 ms: 1.10x faster                                                 |
| tomli_loads          | 2.11 sec                                               | 1.93 sec: 1.09x faster                                                |
| xml_etree_process    | 60.4 ms                                                | 55.5 ms: 1.09x faster                                                 |
| xml_etree_parse      | 156 ms                                                 | 149 ms: 1.05x faster                                                  |
| unpickle             | 14.9 us                                                | 14.3 us: 1.04x faster                                                 |
| xml_etree_iterparse  | 102 ms                                                 | 99.7 ms: 1.02x faster                                                 |
| json_loads           | 27.0 us                                                | 26.5 us: 1.02x faster                                                 |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                                  |
| pickle_list          | 5.01 us                                                | 5.13 us: 1.02x slower                                                 |
| pickle               | 11.6 us                                                | 11.9 us: 1.02x slower                                                 |
| pickle_pure_python   | 300 us                                                 | 313 us: 1.04x slower                                                  |
| pickle_dict          | 33.2 us                                                | 34.8 us: 1.05x slower                                                 |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                 |
| unpickle_list        | 4.96 us                                                | 5.53 us: 1.11x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                | 7.09 ms: 1.01x slower                                                 |
| python_startup         | 10.6 ms                                                | 11.9 ms: 1.13x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.1 ms: 1.10x faster                                                 |
| django_template | 34.4 ms                                                | 36.7 ms: 1.07x slower                                                 |
| genshi_text     | 22.9 ms                                                | 25.2 ms: 1.10x slower                                                 |
| genshi_xml      | 50.3 ms                                                | 61.9 ms: 1.23x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.07x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 274 us: 1.29x faster                                                  |
| deepcopy_memo              | 38.0 us                                                | 29.8 us: 1.27x faster                                                 |
| async_tree_memoization_tg  | 465 ms                                                 | 375 ms: 1.24x faster                                                  |
| richards                   | 48.1 ms                                                | 41.4 ms: 1.16x faster                                                 |
| richards_super             | 54.4 ms                                                | 47.2 ms: 1.15x faster                                                 |
| scimark_fft                | 369 ms                                                 | 323 ms: 1.14x faster                                                  |
| deepcopy_reduce            | 3.17 us                                                | 2.81 us: 1.13x faster                                                 |
| xml_etree_generate         | 87.0 ms                                                | 78.8 ms: 1.10x faster                                                 |
| telco                      | 8.45 ms                                                | 7.69 ms: 1.10x faster                                                 |
| mako                       | 11.1 ms                                                | 10.1 ms: 1.10x faster                                                 |
| tomli_loads                | 2.11 sec                                               | 1.93 sec: 1.09x faster                                                |
| xml_etree_process          | 60.4 ms                                                | 55.5 ms: 1.09x faster                                                 |
| crypto_pyaes               | 73.0 ms                                                | 67.7 ms: 1.08x faster                                                 |
| async_tree_none            | 354 ms                                                 | 329 ms: 1.08x faster                                                  |
| json                       | 5.20 ms                                                | 4.88 ms: 1.06x faster                                                 |
| bpe_tokeniser              | 4.69 sec                                               | 4.44 sec: 1.06x faster                                                |
| go                         | 142 ms                                                 | 134 ms: 1.06x faster                                                  |
| regex_effbot               | 3.88 ms                                                | 3.68 ms: 1.06x faster                                                 |
| pathlib                    | 17.1 ms                                                | 16.2 ms: 1.05x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 420 ms: 1.05x faster                                                  |
| xml_etree_parse            | 156 ms                                                 | 149 ms: 1.05x faster                                                  |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.04x faster                                                  |
| unpickle                   | 14.9 us                                                | 14.3 us: 1.04x faster                                                 |
| scimark_monte_carlo        | 66.3 ms                                                | 63.9 ms: 1.04x faster                                                 |
| logging_silent             | 102 ns                                                 | 98.8 ns: 1.03x faster                                                 |
| float                      | 78.5 ms                                                | 76.0 ms: 1.03x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.90 ms: 1.03x faster                                                 |
| logging_format             | 6.25 us                                                | 6.11 us: 1.02x faster                                                 |
| xml_etree_iterparse        | 102 ms                                                 | 99.7 ms: 1.02x faster                                                 |
| regex_v8                   | 25.3 ms                                                | 24.7 ms: 1.02x faster                                                 |
| scimark_lu                 | 115 ms                                                 | 113 ms: 1.02x faster                                                  |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                  |
| pycparser                  | 1.19 sec                                               | 1.17 sec: 1.02x faster                                                |
| json_loads                 | 27.0 us                                                | 26.5 us: 1.02x faster                                                 |
| nbody                      | 85.7 ms                                                | 84.5 ms: 1.02x faster                                                 |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                                  |
| sqlite_synth               | 2.85 us                                                | 2.81 us: 1.01x faster                                                 |
| pyflate                    | 460 ms                                                 | 455 ms: 1.01x faster                                                  |
| html5lib                   | 64.5 ms                                                | 64.0 ms: 1.01x faster                                                 |
| logging_simple             | 5.66 us                                                | 5.62 us: 1.01x faster                                                 |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x slower                                                  |
| mdp                        | 2.74 sec                                               | 2.75 sec: 1.00x slower                                                |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                                |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                                  |
| coverage                   | 83.7 ms                                                | 84.6 ms: 1.01x slower                                                 |
| python_startup_no_site     | 6.99 ms                                                | 7.09 ms: 1.01x slower                                                 |
| coroutines                 | 22.5 ms                                                | 22.9 ms: 1.02x slower                                                 |
| chaos                      | 58.4 ms                                                | 59.4 ms: 1.02x slower                                                 |
| asyncio_tcp                | 488 ms                                                 | 499 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 556 ms: 1.02x slower                                                  |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                                  |
| pickle_list                | 5.01 us                                                | 5.13 us: 1.02x slower                                                 |
| pickle                     | 11.6 us                                                | 11.9 us: 1.02x slower                                                 |
| pprint_pformat             | 1.51 sec                                               | 1.56 sec: 1.03x slower                                                |
| deltablue                  | 3.15 ms                                                | 3.27 ms: 1.04x slower                                                 |
| tornado_http               | 91.5 ms                                                | 95.0 ms: 1.04x slower                                                 |
| pickle_pure_python         | 300 us                                                 | 313 us: 1.04x slower                                                  |
| typing_runtime_protocols   | 159 us                                                 | 166 us: 1.05x slower                                                  |
| async_generators           | 433 ms                                                 | 454 ms: 1.05x slower                                                  |
| pickle_dict                | 33.2 us                                                | 34.8 us: 1.05x slower                                                 |
| 2to3                       | 265 ms                                                 | 278 ms: 1.05x slower                                                  |
| fannkuch                   | 381 ms                                                 | 401 ms: 1.05x slower                                                  |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.06x slower                                                 |
| dulwich_log                | 63.0 ms                                                | 66.7 ms: 1.06x slower                                                 |
| comprehensions             | 16.4 us                                                | 17.4 us: 1.06x slower                                                 |
| raytrace                   | 262 ms                                                 | 278 ms: 1.06x slower                                                  |
| django_template            | 34.4 ms                                                | 36.7 ms: 1.07x slower                                                 |
| sqlglot_normalize          | 107 ms                                                 | 115 ms: 1.07x slower                                                  |
| sqlglot_transpile          | 1.57 ms                                                | 1.69 ms: 1.07x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                 |
| bench_thread_pool          | 815 us                                                 | 878 us: 1.08x slower                                                  |
| regex_compile              | 131 ms                                                 | 143 ms: 1.09x slower                                                  |
| sympy_expand               | 462 ms                                                 | 505 ms: 1.09x slower                                                  |
| nqueens                    | 80.6 ms                                                | 88.6 ms: 1.10x slower                                                 |
| genshi_text                | 22.9 ms                                                | 25.2 ms: 1.10x slower                                                 |
| sympy_str                  | 274 ms                                                 | 303 ms: 1.11x slower                                                  |
| unpickle_list              | 4.96 us                                                | 5.53 us: 1.11x slower                                                 |
| sqlglot_optimize           | 53.9 ms                                                | 60.6 ms: 1.12x slower                                                 |
| python_startup             | 10.6 ms                                                | 11.9 ms: 1.13x slower                                                 |
| docutils                   | 2.58 sec                                               | 2.92 sec: 1.13x slower                                                |
| hexiom                     | 6.13 ms                                                | 7.07 ms: 1.15x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 175 ms: 1.17x slower                                                  |
| async_tree_io_tg           | 825 ms                                                 | 971 ms: 1.18x slower                                                  |
| gc_traversal               | 3.81 ms                                                | 4.52 ms: 1.19x slower                                                 |
| sympy_integrate            | 19.9 ms                                                | 23.6 ms: 1.19x slower                                                 |
| pylint                     | 313 ms                                                 | 377 ms: 1.20x slower                                                  |
| generators                 | 28.8 ms                                                | 35.2 ms: 1.22x slower                                                 |
| genshi_xml                 | 50.3 ms                                                | 61.9 ms: 1.23x slower                                                 |
| create_gc_cycles           | 1.61 ms                                                | 2.68 ms: 1.67x slower                                                 |
| unpack_sequence            | 42.4 ns                                                | 108 ns: 2.56x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 84.0 ms: 3.50x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.04x slower                                                          |

Benchmark hidden because not significant (6): thrift, async_tree_cpu_io_mixed, pprint_safe_repr, asyncio_websockets, async_tree_none_tg, async_tree_io
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: sphinx

# HPT report

- Reliability score: 86.47% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.19x