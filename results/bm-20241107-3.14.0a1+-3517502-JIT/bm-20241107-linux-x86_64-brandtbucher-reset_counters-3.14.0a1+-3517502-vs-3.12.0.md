# Results vs. 3.12.0

- fork: brandtbucher
- ref: reset_counters
- machine: linux-x86_64
- commit hash: 3517502
- commit date: 2024-11-07
- overall geometric mean: 1.057x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 280 ms: 1.02x slower                                                   |
| docutils       | 2.77 sec                                               | 2.92 sec: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 381 ms: 1.51x faster                                                   |
| async_tree_none            | 472 ms                                                 | 331 ms: 1.42x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 320 ms: 1.40x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 414 ms: 1.39x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 859 ms: 1.35x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 560 ms: 1.30x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 573 ms: 1.27x faster                                                   |
| async_tree_io_tg           | 1.18 sec                                               | 971 ms: 1.22x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 82.4 ms: 1.18x faster                                                  |
| float          | 84.7 ms                                                | 76.6 ms: 1.11x faster                                                  |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 140 ms: 1.06x faster                                                   |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                   |
| regex_effbot   | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                  |
| regex_v8       | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 79.2 ms: 1.13x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 55.8 ms: 1.11x faster                                                  |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                   |
| json_loads           | 28.5 us                                                | 26.6 us: 1.07x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.06x faster                                                   |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                                   |
| pickle_pure_python   | 324 us                                                 | 327 us: 1.01x slower                                                   |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                  |
| django_template | 34.6 ms                                                | 36.1 ms: 1.04x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 381 ms: 1.51x faster                                                   |
| async_tree_none            | 472 ms                                                 | 331 ms: 1.42x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 320 ms: 1.40x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 414 ms: 1.39x faster                                                   |
| deepcopy                   | 371 us                                                 | 267 us: 1.39x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 29.9 us: 1.36x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 859 ms: 1.35x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 560 ms: 1.30x faster                                                   |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.27x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 573 ms: 1.27x faster                                                   |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 971 ms: 1.22x faster                                                   |
| scimark_fft                | 382 ms                                                 | 317 ms: 1.20x faster                                                   |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 68.6 ms: 1.19x faster                                                  |
| logging_format             | 7.23 us                                                | 6.13 us: 1.18x faster                                                  |
| nbody                      | 97.0 ms                                                | 82.4 ms: 1.18x faster                                                  |
| mako                       | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 64.4 ms: 1.17x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.59 us: 1.16x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.29 ms: 1.13x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 79.2 ms: 1.13x faster                                                  |
| chaos                      | 67.0 ms                                                | 59.5 ms: 1.13x faster                                                  |
| raytrace                   | 312 ms                                                 | 278 ms: 1.12x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.51 ms: 1.12x faster                                                  |
| richards                   | 45.8 ms                                                | 41.1 ms: 1.12x faster                                                  |
| float                      | 84.7 ms                                                | 76.6 ms: 1.11x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 55.8 ms: 1.11x faster                                                  |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.08x faster                                                   |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                   |
| fannkuch                   | 417 ms                                                 | 388 ms: 1.07x faster                                                   |
| json_loads                 | 28.5 us                                                | 26.6 us: 1.07x faster                                                  |
| pyflate                    | 482 ms                                                 | 451 ms: 1.07x faster                                                   |
| richards_super             | 51.5 ms                                                | 48.2 ms: 1.07x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.06x faster                                                   |
| regex_compile              | 148 ms                                                 | 140 ms: 1.06x faster                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.8 ms: 1.05x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                                   |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                   |
| go                         | 139 ms                                                 | 134 ms: 1.04x faster                                                   |
| logging_silent             | 104 ns                                                 | 100 ns: 1.04x faster                                                   |
| json                       | 5.26 ms                                                | 5.06 ms: 1.04x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.04x faster                                                   |
| pprint_safe_repr           | 776 ms                                                 | 749 ms: 1.03x faster                                                   |
| coroutines                 | 23.2 ms                                                | 22.4 ms: 1.03x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.03x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.53 sec: 1.03x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.16 sec: 1.02x faster                                                 |
| sqlite_synth               | 2.83 us                                                | 2.78 us: 1.02x faster                                                  |
| async_generators           | 463 ms                                                 | 457 ms: 1.01x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 67.7 ms: 1.01x faster                                                  |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| sympy_str                  | 300 ms                                                 | 301 ms: 1.00x slower                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 148 ms: 1.01x slower                                                   |
| pickle_pure_python         | 324 us                                                 | 327 us: 1.01x slower                                                   |
| asyncio_websockets         | 551 ms                                                 | 558 ms: 1.01x slower                                                   |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                   |
| regex_effbot               | 3.61 ms                                                | 3.68 ms: 1.02x slower                                                  |
| 2to3                       | 274 ms                                                 | 280 ms: 1.02x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.12 ms: 1.03x slower                                                  |
| sympy_sum                  | 169 ms                                                 | 174 ms: 1.03x slower                                                   |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.03x slower                                                   |
| django_template            | 34.6 ms                                                | 36.1 ms: 1.04x slower                                                  |
| mdp                        | 2.63 sec                                               | 2.76 sec: 1.05x slower                                                 |
| sympy_expand               | 478 ms                                                 | 503 ms: 1.05x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                  |
| nqueens                    | 83.3 ms                                                | 88.0 ms: 1.06x slower                                                  |
| docutils                   | 2.77 sec                                               | 2.92 sec: 1.06x slower                                                 |
| bench_thread_pool          | 842 us                                                 | 891 us: 1.06x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                  |
| telco                      | 7.10 ms                                                | 7.60 ms: 1.07x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.07x slower                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 59.6 ms: 1.09x slower                                                  |
| sympy_integrate            | 21.4 ms                                                | 23.3 ms: 1.09x slower                                                  |
| hexiom                     | 6.41 ms                                                | 7.07 ms: 1.10x slower                                                  |
| generators                 | 31.2 ms                                                | 35.9 ms: 1.15x slower                                                  |
| coverage                   | 72.7 ms                                                | 85.7 ms: 1.18x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.67 ms: 1.23x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.69 ms: 1.82x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 84.6 ms: 3.52x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (2): spectral_norm, sqlglot_transpile
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (10) of results/bm-20241107-3.14.0a1+-3517502-JIT/bm-20241107-linux-x86_64-brandtbucher-reset_counters-3.14.0a1+-3517502.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, pylint, shortest_path, sphinx, thrift

- Geometric mean (including insignificant results): 1.057x faster
# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.15x