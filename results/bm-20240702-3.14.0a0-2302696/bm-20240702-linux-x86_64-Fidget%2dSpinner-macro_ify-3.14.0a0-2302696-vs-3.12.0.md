# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: macro_ify
- machine: linux-x86_64
- commit hash: 2302696
- commit date: 2024-07-02
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                                 |
| docutils       | 2.77 sec                                               | 2.68 sec: 1.03x faster                                               |
| tornado_http   | 103 ms                                                 | 90.3 ms: 1.14x faster                                                |
| Geometric mean | (ref)                                                  | 1.07x faster                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 378 ms: 1.52x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.50x faster                                                 |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 405 ms: 1.43x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 846 ms: 1.40x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 844 ms: 1.37x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 538 ms: 1.35x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.41x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 86.4 ms: 1.12x faster                                                |
| float          | 84.7 ms                                                | 76.5 ms: 1.11x faster                                                |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                 |
| regex_effbot   | 3.61 ms                                                | 3.64 ms: 1.01x slower                                                |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                                 |
| regex_v8       | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.12 sec: 1.10x faster                                               |
| unpickle_pure_python | 230 us                                                 | 213 us: 1.08x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 85.2 ms: 1.05x faster                                                |
| json_loads           | 28.5 us                                                | 27.5 us: 1.04x faster                                                |
| xml_etree_process    | 61.7 ms                                                | 59.8 ms: 1.03x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 156 ms: 1.02x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                                 |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                |
| python_startup         | 9.55 ms                                                | 10.4 ms: 1.09x slower                                                |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                |
| django_template | 34.6 ms                                                | 33.9 ms: 1.02x faster                                                |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 378 ms: 1.52x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 299 ms: 1.50x faster                                                 |
| async_tree_none            | 472 ms                                                 | 323 ms: 1.46x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 405 ms: 1.43x faster                                                 |
| deepcopy                   | 371 us                                                 | 263 us: 1.41x faster                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 846 ms: 1.40x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 844 ms: 1.37x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 30.0 us: 1.36x faster                                                |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 538 ms: 1.35x faster                                                 |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 561 ms: 1.29x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                |
| pathlib                    | 19.3 ms                                                | 15.7 ms: 1.23x faster                                                |
| raytrace                   | 312 ms                                                 | 260 ms: 1.20x faster                                                 |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                                |
| logging_simple             | 6.46 us                                                | 5.52 us: 1.17x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.17 ms: 1.17x faster                                                |
| chaos                      | 67.0 ms                                                | 57.9 ms: 1.16x faster                                                |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                 |
| tornado_http               | 103 ms                                                 | 90.3 ms: 1.14x faster                                                |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 66.6 ms: 1.13x faster                                                |
| nbody                      | 97.0 ms                                                | 86.4 ms: 1.12x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 73.1 ms: 1.12x faster                                                |
| sympy_str                  | 300 ms                                                 | 270 ms: 1.11x faster                                                 |
| float                      | 84.7 ms                                                | 76.5 ms: 1.11x faster                                                |
| tomli_loads                | 2.33 sec                                               | 2.12 sec: 1.10x faster                                               |
| sympy_integrate            | 21.4 ms                                                | 19.7 ms: 1.09x faster                                                |
| generators                 | 31.2 ms                                                | 28.7 ms: 1.09x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.65 ms: 1.09x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 213 us: 1.08x faster                                                 |
| fannkuch                   | 417 ms                                                 | 387 ms: 1.08x faster                                                 |
| async_generators           | 463 ms                                                 | 431 ms: 1.07x faster                                                 |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                                |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.57 ms: 1.07x faster                                                |
| scimark_fft                | 382 ms                                                 | 357 ms: 1.07x faster                                                 |
| pyflate                    | 482 ms                                                 | 451 ms: 1.07x faster                                                 |
| bench_thread_pool          | 842 us                                                 | 788 us: 1.07x faster                                                 |
| dulwich_log                | 68.5 ms                                                | 64.3 ms: 1.07x faster                                                |
| gc_traversal               | 3.79 ms                                                | 3.57 ms: 1.06x faster                                                |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                 |
| nqueens                    | 83.3 ms                                                | 78.8 ms: 1.06x faster                                                |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                                |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                               |
| mdp                        | 2.63 sec                                               | 2.51 sec: 1.05x faster                                               |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 85.2 ms: 1.05x faster                                                |
| pprint_safe_repr           | 776 ms                                                 | 743 ms: 1.04x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.04x faster                                                 |
| dask                       | 372 ms                                                 | 357 ms: 1.04x faster                                                 |
| json_loads                 | 28.5 us                                                | 27.5 us: 1.04x faster                                                |
| sympy_expand               | 478 ms                                                 | 461 ms: 1.04x faster                                                 |
| scimark_sor                | 129 ms                                                 | 125 ms: 1.04x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                               |
| docutils                   | 2.77 sec                                               | 2.68 sec: 1.03x faster                                               |
| hexiom                     | 6.41 ms                                                | 6.20 ms: 1.03x faster                                                |
| xml_etree_process          | 61.7 ms                                                | 59.8 ms: 1.03x faster                                                |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                                 |
| sqlglot_optimize           | 54.8 ms                                                | 53.5 ms: 1.02x faster                                                |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.02x faster                                                 |
| xml_etree_parse            | 159 ms                                                 | 156 ms: 1.02x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                                 |
| django_template            | 34.6 ms                                                | 33.9 ms: 1.02x faster                                                |
| json                       | 5.26 ms                                                | 5.16 ms: 1.02x faster                                                |
| asyncio_tcp                | 491 ms                                                 | 487 ms: 1.01x faster                                                 |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.79 sec: 1.00x slower                                               |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                 |
| go                         | 139 ms                                                 | 140 ms: 1.01x slower                                                 |
| regex_effbot               | 3.61 ms                                                | 3.64 ms: 1.01x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.01x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.02 ms: 1.01x slower                                                |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                |
| richards_super             | 51.5 ms                                                | 52.2 ms: 1.01x slower                                                |
| coroutines                 | 23.2 ms                                                | 23.6 ms: 1.02x slower                                                |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 24.5 ms: 1.06x slower                                                |
| python_startup             | 9.55 ms                                                | 10.4 ms: 1.09x slower                                                |
| telco                      | 7.10 ms                                                | 8.27 ms: 1.17x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 1.72 ms: 1.17x slower                                                |
| coverage                   | 72.7 ms                                                | 92.3 ms: 1.27x slower                                                |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                         |

Benchmark hidden because not significant (3): logging_silent, bench_mp_pool, richards
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240702-3.14.0a0-2302696/bm-20240702-linux-x86_64-Fidget%2dSpinner-macro_ify-3.14.0a0-2302696.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.98x