# Results vs. 3.12.0

- fork: python
- ref: 0cd4befb02df07c0b320
- machine: linux-x86_64
- commit hash: 0cd4bef
- commit date: 2025-03-31
- overall geometric mean: 1.129x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                                   |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 613 ms: 1.93x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 613 ms: 1.89x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                   |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.81x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 63.9 ms: 1.33x faster                                                  |
| nbody          | 97.0 ms                                                | 85.6 ms: 1.13x faster                                                  |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.37 ms: 1.07x faster                                                  |
| regex_v8       | 23.1 ms                                                | 23.0 ms: 1.01x faster                                                  |
| regex_dna      | 212 ms                                                 | 218 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.85 sec: 1.26x faster                                                 |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 79.8 ms: 1.12x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 97.4 ms: 1.10x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 212 us: 1.09x faster                                                   |
| json_loads           | 28.5 us                                                | 29.7 us: 1.04x slower                                                  |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                           |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.22 ms: 1.18x slower                                                  |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                  |
| django_template | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.25 sec: 2.10x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 613 ms: 1.93x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 613 ms: 1.89x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                   |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.81x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                                   |
| deepcopy                   | 371 us                                                 | 255 us: 1.45x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 29.8 us: 1.37x faster                                                  |
| float                      | 84.7 ms                                                | 63.9 ms: 1.33x faster                                                  |
| richards                   | 45.8 ms                                                | 35.5 ms: 1.29x faster                                                  |
| richards_super             | 51.5 ms                                                | 40.6 ms: 1.27x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.85 sec: 1.26x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.25x faster                                                  |
| scimark_fft                | 382 ms                                                 | 307 ms: 1.24x faster                                                   |
| deltablue                  | 3.72 ms                                                | 3.03 ms: 1.23x faster                                                  |
| spectral_norm              | 115 ms                                                 | 94.0 ms: 1.22x faster                                                  |
| comprehensions             | 21.8 us                                                | 18.5 us: 1.18x faster                                                  |
| raytrace                   | 312 ms                                                 | 267 ms: 1.17x faster                                                   |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                   |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                                  |
| logging_format             | 7.23 us                                                | 6.28 us: 1.15x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.64 us: 1.14x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 60.5 ms: 1.13x faster                                                  |
| nbody                      | 97.0 ms                                                | 85.6 ms: 1.13x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.49 ms: 1.13x faster                                                  |
| chaos                      | 67.0 ms                                                | 59.5 ms: 1.13x faster                                                  |
| pyflate                    | 482 ms                                                 | 429 ms: 1.12x faster                                                   |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                   |
| xml_etree_generate         | 89.2 ms                                                | 79.8 ms: 1.12x faster                                                  |
| async_generators           | 463 ms                                                 | 416 ms: 1.11x faster                                                   |
| generators                 | 31.2 ms                                                | 28.1 ms: 1.11x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 67.8 ms: 1.11x faster                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.11x faster                                                   |
| go                         | 139 ms                                                 | 126 ms: 1.11x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 74.5 ms: 1.10x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 56.2 ms: 1.10x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 97.4 ms: 1.10x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.6 ms: 1.09x faster                                                  |
| sympy_str                  | 300 ms                                                 | 274 ms: 1.09x faster                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.2 ms: 1.09x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 212 us: 1.09x faster                                                   |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.37 ms: 1.07x faster                                                  |
| django_template            | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                  |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.07x faster                                                   |
| logging_silent             | 104 ns                                                 | 97.8 ns: 1.07x faster                                                  |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                   |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.72 us: 1.04x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                 |
| fannkuch                   | 417 ms                                                 | 408 ms: 1.02x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.01x faster                                                   |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                   |
| regex_v8                   | 23.1 ms                                                | 23.0 ms: 1.01x faster                                                  |
| sympy_expand               | 478 ms                                                 | 475 ms: 1.01x faster                                                   |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                                  |
| regex_dna                  | 212 ms                                                 | 218 ms: 1.03x slower                                                   |
| json_loads                 | 28.5 us                                                | 29.7 us: 1.04x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 885 us: 1.05x slower                                                   |
| hexiom                     | 6.41 ms                                                | 6.81 ms: 1.06x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 170 us: 1.08x slower                                                   |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                  |
| telco                      | 7.10 ms                                                | 7.89 ms: 1.11x slower                                                  |
| coverage                   | 72.7 ms                                                | 85.4 ms: 1.18x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 8.22 ms: 1.18x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 5.06 ms: 1.33x slower                                                  |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.69x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 83.1 ms: 3.46x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                           |

Benchmark hidden because not significant (7): pprint_safe_repr, nqueens, pickle_pure_python, asyncio_websockets, pprint_pformat, json, pycparser
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250331-3.14.0a6+-0cd4bef-JIT/bm-20250331-linux-x86_64-python-0cd4befb02df07c0b320-3.14.0a6+-0cd4bef.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.129x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.12x