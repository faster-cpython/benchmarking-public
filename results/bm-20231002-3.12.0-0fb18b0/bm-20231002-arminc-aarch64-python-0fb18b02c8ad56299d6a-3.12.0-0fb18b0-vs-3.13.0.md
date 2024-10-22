# Results vs. 3.13.0

- fork: python
- ref: 0fb18b02c8ad56299d6a
- machine: linux-aarch64
- commit hash: 0fb18b0
- commit date: 2023-10-02
- overall geometric mean: 1.01x slower
- HPT reliability: 97.91%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 308 ms: 1.01x slower                                                  |
| chameleon      | 9.02 ms                                                  | 8.81 ms: 1.02x faster                                                 |
| docutils       | 2.91 sec                                                 | 2.98 sec: 1.03x slower                                                |
| Geometric mean | (ref)                                                    | 1.01x slower                                                          |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_generators           | 496 ms                                                   | 491 ms: 1.01x faster                                                  |
| coroutines                 | 28.2 ms                                                  | 29.0 ms: 1.03x slower                                                 |
| async_tree_memoization_tg  | 649 ms                                                   | 740 ms: 1.14x slower                                                  |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 912 ms: 1.19x slower                                                  |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 884 ms: 1.20x slower                                                  |
| async_tree_none_tg         | 467 ms                                                   | 577 ms: 1.23x slower                                                  |
| async_tree_memoization     | 626 ms                                                   | 777 ms: 1.24x slower                                                  |
| async_tree_none            | 493 ms                                                   | 624 ms: 1.26x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.41 sec: 1.28x slower                                                |
| async_tree_io_tg           | 1.09 sec                                                 | 1.40 sec: 1.29x slower                                                |
| Geometric mean             | (ref)                                                    | 1.14x slower                                                          |

Benchmark hidden because not significant (3): asyncio_tcp, asyncio_tcp_ssl, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 105 ms: 1.09x faster                                                  |
| float          | 94.4 ms                                                  | 92.1 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                    | 1.04x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 31.5 ms                                                  | 28.3 ms: 1.11x faster                                                 |
| regex_effbot   | 4.87 ms                                                  | 4.64 ms: 1.05x faster                                                 |
| regex_dna      | 246 ms                                                   | 254 ms: 1.03x slower                                                  |
| regex_compile  | 128 ms                                                   | 137 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                    | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|----------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle             | 20.2 us                                                  | 18.5 us: 1.09x faster                                                 |
| json_dumps           | 13.4 ms                                                  | 12.3 ms: 1.09x faster                                                 |
| unpickle_list        | 6.65 us                                                  | 6.17 us: 1.08x faster                                                 |
| json_loads           | 31.4 us                                                  | 30.7 us: 1.02x faster                                                 |
| pickle_dict          | 38.1 us                                                  | 37.3 us: 1.02x faster                                                 |
| pickle_list          | 5.34 us                                                  | 5.25 us: 1.02x faster                                                 |
| pickle_pure_python   | 359 us                                                   | 365 us: 1.02x slower                                                  |
| unpickle_pure_python | 254 us                                                   | 260 us: 1.02x slower                                                  |
| tomli_loads          | 2.53 sec                                                 | 2.59 sec: 1.03x slower                                                |
| xml_etree_iterparse  | 147 ms                                                   | 150 ms: 1.03x slower                                                  |
| xml_etree_parse      | 188 ms                                                   | 195 ms: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                    | 1.02x faster                                                          |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_generate, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 11.4 ms: 1.17x faster                                                 |
| python_startup_no_site | 8.75 ms                                                  | 8.37 ms: 1.05x faster                                                 |
| Geometric mean         | (ref)                                                    | 1.10x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|-----------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 42.3 ms                                                  | 40.7 ms: 1.04x faster                                                 |
| mako            | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                                 |
| genshi_text     | 27.7 ms                                                  | 27.4 ms: 1.01x faster                                                 |
| genshi_xml      | 60.2 ms                                                  | 60.6 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                    | 1.02x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 |
|----------------------------|:--------------------------------------------------------:|:---------------------------------------------------------------------:|
| mypy2                      | 1.18 sec                                                 | 873 ms: 1.35x faster                                                  |
| python_startup             | 13.3 ms                                                  | 11.4 ms: 1.17x faster                                                 |
| telco                      | 9.73 ms                                                  | 8.51 ms: 1.14x faster                                                 |
| coverage                   | 98.5 ms                                                  | 87.3 ms: 1.13x faster                                                 |
| regex_v8                   | 31.5 ms                                                  | 28.3 ms: 1.11x faster                                                 |
| create_gc_cycles           | 2.12 ms                                                  | 1.92 ms: 1.11x faster                                                 |
| unpickle                   | 20.2 us                                                  | 18.5 us: 1.09x faster                                                 |
| nbody                      | 114 ms                                                   | 105 ms: 1.09x faster                                                  |
| json_dumps                 | 13.4 ms                                                  | 12.3 ms: 1.09x faster                                                 |
| spectral_norm              | 141 ms                                                   | 131 ms: 1.08x faster                                                  |
| unpickle_list              | 6.65 us                                                  | 6.17 us: 1.08x faster                                                 |
| scimark_fft                | 447 ms                                                   | 418 ms: 1.07x faster                                                  |
| logging_silent             | 135 ns                                                   | 127 ns: 1.07x faster                                                  |
| typing_runtime_protocols   | 192 us                                                   | 181 us: 1.06x faster                                                  |
| scimark_sor                | 159 ms                                                   | 150 ms: 1.06x faster                                                  |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 6.19 ms: 1.06x faster                                                 |
| gunicorn                   | 1.20 ms                                                  | 1.14 ms: 1.06x faster                                                 |
| richards                   | 53.5 ms                                                  | 50.9 ms: 1.05x faster                                                 |
| regex_effbot               | 4.87 ms                                                  | 4.64 ms: 1.05x faster                                                 |
| python_startup_no_site     | 8.75 ms                                                  | 8.37 ms: 1.05x faster                                                 |
| django_template            | 42.3 ms                                                  | 40.7 ms: 1.04x faster                                                 |
| bench_mp_pool              | 7.30 ms                                                  | 7.05 ms: 1.03x faster                                                 |
| go                         | 163 ms                                                   | 157 ms: 1.03x faster                                                  |
| mako                       | 13.3 ms                                                  | 12.9 ms: 1.03x faster                                                 |
| richards_super             | 60.3 ms                                                  | 58.5 ms: 1.03x faster                                                 |
| gc_traversal               | 4.53 ms                                                  | 4.40 ms: 1.03x faster                                                 |
| deepcopy_memo              | 51.0 us                                                  | 49.6 us: 1.03x faster                                                 |
| float                      | 94.4 ms                                                  | 92.1 ms: 1.03x faster                                                 |
| json_loads                 | 31.4 us                                                  | 30.7 us: 1.02x faster                                                 |
| chameleon                  | 9.02 ms                                                  | 8.81 ms: 1.02x faster                                                 |
| hexiom                     | 7.13 ms                                                  | 6.98 ms: 1.02x faster                                                 |
| pickle_dict                | 38.1 us                                                  | 37.3 us: 1.02x faster                                                 |
| sqlglot_normalize          | 128 ms                                                   | 126 ms: 1.02x faster                                                  |
| sqlite_synth               | 3.84 us                                                  | 3.77 us: 1.02x faster                                                 |
| fannkuch                   | 452 ms                                                   | 443 ms: 1.02x faster                                                  |
| pickle_list                | 5.34 us                                                  | 5.25 us: 1.02x faster                                                 |
| sqlglot_optimize           | 62.4 ms                                                  | 61.3 ms: 1.02x faster                                                 |
| meteor_contest             | 113 ms                                                   | 112 ms: 1.01x faster                                                  |
| json                       | 5.61 ms                                                  | 5.54 ms: 1.01x faster                                                 |
| deepcopy                   | 451 us                                                   | 446 us: 1.01x faster                                                  |
| async_generators           | 496 ms                                                   | 491 ms: 1.01x faster                                                  |
| pprint_safe_repr           | 926 ms                                                   | 916 ms: 1.01x faster                                                  |
| genshi_text                | 27.7 ms                                                  | 27.4 ms: 1.01x faster                                                 |
| thrift                     | 946 us                                                   | 937 us: 1.01x faster                                                  |
| pprint_pformat             | 1.90 sec                                                 | 1.88 sec: 1.01x faster                                                |
| pyflate                    | 556 ms                                                   | 559 ms: 1.01x slower                                                  |
| genshi_xml                 | 60.2 ms                                                  | 60.6 ms: 1.01x slower                                                 |
| 2to3                       | 306 ms                                                   | 308 ms: 1.01x slower                                                  |
| deepcopy_reduce            | 4.07 us                                                  | 4.10 us: 1.01x slower                                                 |
| mdp                        | 3.36 sec                                                 | 3.41 sec: 1.01x slower                                                |
| scimark_monte_carlo        | 83.8 ms                                                  | 85.1 ms: 1.01x slower                                                 |
| pickle_pure_python         | 359 us                                                   | 365 us: 1.02x slower                                                  |
| unpickle_pure_python       | 254 us                                                   | 260 us: 1.02x slower                                                  |
| bench_thread_pool          | 1.28 ms                                                  | 1.31 ms: 1.03x slower                                                 |
| tomli_loads                | 2.53 sec                                                 | 2.59 sec: 1.03x slower                                                |
| xml_etree_iterparse        | 147 ms                                                   | 150 ms: 1.03x slower                                                  |
| docutils                   | 2.91 sec                                                 | 2.98 sec: 1.03x slower                                                |
| coroutines                 | 28.2 ms                                                  | 29.0 ms: 1.03x slower                                                 |
| sympy_integrate            | 21.0 ms                                                  | 21.6 ms: 1.03x slower                                                 |
| regex_dna                  | 246 ms                                                   | 254 ms: 1.03x slower                                                  |
| chaos                      | 68.8 ms                                                  | 71.4 ms: 1.04x slower                                                 |
| xml_etree_parse            | 188 ms                                                   | 195 ms: 1.04x slower                                                  |
| scimark_lu                 | 139 ms                                                   | 146 ms: 1.04x slower                                                  |
| crypto_pyaes               | 82.7 ms                                                  | 86.6 ms: 1.05x slower                                                 |
| sqlglot_transpile          | 1.73 ms                                                  | 1.83 ms: 1.06x slower                                                 |
| sqlglot_parse              | 1.38 ms                                                  | 1.46 ms: 1.06x slower                                                 |
| sympy_str                  | 264 ms                                                   | 280 ms: 1.06x slower                                                  |
| logging_format             | 7.83 us                                                  | 8.34 us: 1.07x slower                                                 |
| regex_compile              | 128 ms                                                   | 137 ms: 1.07x slower                                                  |
| deltablue                  | 3.85 ms                                                  | 4.12 ms: 1.07x slower                                                 |
| dask                       | 350 ms                                                   | 376 ms: 1.07x slower                                                  |
| sympy_sum                  | 143 ms                                                   | 154 ms: 1.08x slower                                                  |
| logging_simple             | 7.04 us                                                  | 7.63 us: 1.08x slower                                                 |
| pathlib                    | 22.4 ms                                                  | 24.5 ms: 1.10x slower                                                 |
| async_tree_memoization_tg  | 649 ms                                                   | 740 ms: 1.14x slower                                                  |
| generators                 | 37.8 ms                                                  | 43.5 ms: 1.15x slower                                                 |
| raytrace                   | 298 ms                                                   | 353 ms: 1.19x slower                                                  |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 912 ms: 1.19x slower                                                  |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 884 ms: 1.20x slower                                                  |
| async_tree_none_tg         | 467 ms                                                   | 577 ms: 1.23x slower                                                  |
| async_tree_memoization     | 626 ms                                                   | 777 ms: 1.24x slower                                                  |
| comprehensions             | 20.4 us                                                  | 25.4 us: 1.25x slower                                                 |
| async_tree_none            | 493 ms                                                   | 624 ms: 1.26x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.41 sec: 1.28x slower                                                |
| async_tree_io_tg           | 1.09 sec                                                 | 1.40 sec: 1.29x slower                                                |
| Geometric mean             | (ref)                                                    | 1.01x slower                                                          |

Benchmark hidden because not significant (14): aiohttp, xml_etree_process, xml_etree_generate, pidigits, pycparser, pickle, asyncio_tcp, sympy_expand, asyncio_tcp_ssl, asyncio_websockets, nqueens, html5lib, tornado_http, pylint
Ignored benchmarks (3) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, flaskblogging, unpack_sequence
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: dulwich_log, sqlalchemy_declarative, sqlalchemy_imperative

# HPT report

- Reliability score: 97.91% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x