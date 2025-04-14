# Results vs. 3.12.0

- fork: python
- ref: v3.13.0b4
- machine: linux-x86_64
- commit hash: 567c38b
- commit date: 2024-07-18
- overall geometric mean: 1.060x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 265 ms: 1.04x faster                                       |
| chameleon      | 7.41 ms                                                | 6.96 ms: 1.07x faster                                      |
| docutils       | 2.77 sec                                               | 2.75 sec: 1.01x faster                                     |
| tornado_http   | 103 ms                                                 | 91.7 ms: 1.12x faster                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 325 ms: 1.38x faster                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 429 ms: 1.34x faster                                       |
| async_tree_io_tg           | 1.18 sec                                               | 901 ms: 1.31x faster                                       |
| async_tree_none            | 472 ms                                                 | 366 ms: 1.29x faster                                       |
| async_tree_io              | 1.16 sec                                               | 902 ms: 1.28x faster                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 570 ms: 1.27x faster                                       |
| async_tree_memoization     | 578 ms                                                 | 455 ms: 1.27x faster                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 595 ms: 1.22x faster                                       |
| Geometric mean             | (ref)                                                  | 1.29x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 85.6 ms: 1.13x faster                                      |
| float          | 84.7 ms                                                | 76.8 ms: 1.10x faster                                      |
| pidigits       | 187 ms                                                 | 186 ms: 1.00x faster                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 132 ms: 1.13x faster                                       |
| regex_effbot   | 3.61 ms                                                | 3.77 ms: 1.04x slower                                      |
| regex_v8       | 23.1 ms                                                | 25.2 ms: 1.09x slower                                      |
| regex_dna      | 212 ms                                                 | 232 ms: 1.10x slower                                       |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.13 sec: 1.09x faster                                     |
| pickle_pure_python   | 324 us                                                 | 303 us: 1.07x faster                                       |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                       |
| xml_etree_generate   | 89.2 ms                                                | 87.3 ms: 1.02x faster                                      |
| json_loads           | 28.5 us                                                | 27.9 us: 1.02x faster                                      |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                       |
| xml_etree_process    | 61.7 ms                                                | 60.9 ms: 1.01x faster                                      |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                      |
| Geometric mean       | (ref)                                                  | 1.03x faster                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.10 ms: 1.02x slower                                      |
| python_startup         | 9.55 ms                                                | 10.5 ms: 1.10x slower                                      |
| Geometric mean         | (ref)                                                  | 1.06x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                      |
| django_template | 34.6 ms                                                | 34.1 ms: 1.02x faster                                      |
| Geometric mean  | (ref)                                                  | 1.05x faster                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 325 ms: 1.38x faster                                       |
| async_tree_memoization_tg  | 575 ms                                                 | 429 ms: 1.34x faster                                       |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                      |
| async_tree_io_tg           | 1.18 sec                                               | 901 ms: 1.31x faster                                       |
| async_tree_none            | 472 ms                                                 | 366 ms: 1.29x faster                                       |
| async_tree_io              | 1.16 sec                                               | 902 ms: 1.28x faster                                       |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 570 ms: 1.27x faster                                       |
| async_tree_memoization     | 578 ms                                                 | 455 ms: 1.27x faster                                       |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 595 ms: 1.22x faster                                       |
| raytrace                   | 312 ms                                                 | 264 ms: 1.18x faster                                       |
| logging_format             | 7.23 us                                                | 6.23 us: 1.16x faster                                      |
| mypy2                      | 830 ms                                                 | 717 ms: 1.16x faster                                       |
| logging_simple             | 6.46 us                                                | 5.64 us: 1.15x faster                                      |
| deltablue                  | 3.72 ms                                                | 3.25 ms: 1.14x faster                                      |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                      |
| nbody                      | 97.0 ms                                                | 85.6 ms: 1.13x faster                                      |
| regex_compile              | 148 ms                                                 | 132 ms: 1.13x faster                                       |
| chaos                      | 67.0 ms                                                | 59.5 ms: 1.13x faster                                      |
| tornado_http               | 103 ms                                                 | 91.7 ms: 1.12x faster                                      |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                       |
| float                      | 84.7 ms                                                | 76.8 ms: 1.10x faster                                      |
| crypto_pyaes               | 81.9 ms                                                | 74.4 ms: 1.10x faster                                      |
| sympy_str                  | 300 ms                                                 | 274 ms: 1.09x faster                                       |
| tomli_loads                | 2.33 sec                                               | 2.13 sec: 1.09x faster                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 69.1 ms: 1.09x faster                                      |
| generators                 | 31.2 ms                                                | 28.8 ms: 1.08x faster                                      |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                      |
| dulwich_log                | 68.5 ms                                                | 63.7 ms: 1.08x faster                                      |
| sympy_integrate            | 21.4 ms                                                | 19.9 ms: 1.07x faster                                      |
| async_generators           | 463 ms                                                 | 432 ms: 1.07x faster                                       |
| pprint_safe_repr           | 776 ms                                                 | 724 ms: 1.07x faster                                       |
| pickle_pure_python         | 324 us                                                 | 303 us: 1.07x faster                                       |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                       |
| chameleon                  | 7.41 ms                                                | 6.96 ms: 1.07x faster                                      |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.06x faster                                     |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.06x faster                                      |
| deepcopy_memo              | 40.7 us                                                | 38.5 us: 1.06x faster                                      |
| sqlglot_parse              | 1.36 ms                                                | 1.29 ms: 1.06x faster                                      |
| nqueens                    | 83.3 ms                                                | 78.9 ms: 1.06x faster                                      |
| json                       | 5.26 ms                                                | 5.01 ms: 1.05x faster                                      |
| hexiom                     | 6.41 ms                                                | 6.12 ms: 1.05x faster                                      |
| deepcopy_reduce            | 3.35 us                                                | 3.21 us: 1.04x faster                                      |
| deepcopy                   | 371 us                                                 | 357 us: 1.04x faster                                       |
| sympy_expand               | 478 ms                                                 | 460 ms: 1.04x faster                                       |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                       |
| fannkuch                   | 417 ms                                                 | 402 ms: 1.04x faster                                       |
| 2to3                       | 274 ms                                                 | 265 ms: 1.04x faster                                       |
| bench_thread_pool          | 842 us                                                 | 814 us: 1.03x faster                                       |
| scimark_fft                | 382 ms                                                 | 370 ms: 1.03x faster                                       |
| dask                       | 372 ms                                                 | 361 ms: 1.03x faster                                       |
| sqlglot_normalize          | 110 ms                                                 | 107 ms: 1.03x faster                                       |
| coroutines                 | 23.2 ms                                                | 22.6 ms: 1.02x faster                                      |
| xml_etree_generate         | 89.2 ms                                                | 87.3 ms: 1.02x faster                                      |
| json_loads                 | 28.5 us                                                | 27.9 us: 1.02x faster                                      |
| sqlglot_optimize           | 54.8 ms                                                | 53.7 ms: 1.02x faster                                      |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                       |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                       |
| django_template            | 34.6 ms                                                | 34.1 ms: 1.02x faster                                      |
| gc_traversal               | 3.79 ms                                                | 3.74 ms: 1.01x faster                                      |
| xml_etree_process          | 61.7 ms                                                | 60.9 ms: 1.01x faster                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.01 ms: 1.01x faster                                      |
| docutils                   | 2.77 sec                                               | 2.75 sec: 1.01x faster                                     |
| pidigits                   | 187 ms                                                 | 186 ms: 1.00x faster                                       |
| logging_silent             | 104 ns                                                 | 104 ns: 1.00x faster                                       |
| asyncio_tcp                | 491 ms                                                 | 492 ms: 1.00x slower                                       |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                       |
| go                         | 139 ms                                                 | 141 ms: 1.01x slower                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                     |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                      |
| mdp                        | 2.63 sec                                               | 2.67 sec: 1.01x slower                                     |
| scimark_sor                | 129 ms                                                 | 131 ms: 1.02x slower                                       |
| python_startup_no_site     | 6.94 ms                                                | 7.10 ms: 1.02x slower                                      |
| regex_effbot               | 3.61 ms                                                | 3.77 ms: 1.04x slower                                      |
| richards                   | 45.8 ms                                                | 48.0 ms: 1.05x slower                                      |
| richards_super             | 51.5 ms                                                | 54.2 ms: 1.05x slower                                      |
| regex_v8                   | 23.1 ms                                                | 25.2 ms: 1.09x slower                                      |
| regex_dna                  | 212 ms                                                 | 232 ms: 1.10x slower                                       |
| python_startup             | 9.55 ms                                                | 10.5 ms: 1.10x slower                                      |
| telco                      | 7.10 ms                                                | 8.34 ms: 1.18x slower                                      |
| create_gc_cycles           | 1.48 ms                                                | 1.78 ms: 1.20x slower                                      |
| coverage                   | 72.7 ms                                                | 91.7 ms: 1.26x slower                                      |
| Geometric mean             | (ref)                                                  | 1.06x faster                                               |

Benchmark hidden because not significant (6): xml_etree_parse, pyflate, bench_mp_pool, spectral_norm, pycparser, typing_runtime_protocols
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20240718-3.13.0b4-567c38b/bm-20240718-linux-x86_64-python-v3.13.0b4-3.13.0b4-567c38b.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.060x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.99x