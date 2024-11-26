# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a2
- machine: darwin-arm64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.011x slower
- HPT reliability: 87.28%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.55x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 176 ms: 1.04x slower                                       |
| chameleon      | 4.70 ms                                                | 4.75 ms: 1.01x slower                                      |
| docutils       | 1.50 sec                                               | 1.45 sec: 1.03x faster                                     |
| tornado_http   | 69.3 ms                                                | 86.2 ms: 1.24x slower                                      |
| Geometric mean | (ref)                                                  | 1.06x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none            | 266 ms                                                 | 256 ms: 1.04x faster                                       |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 542 ms: 1.02x slower                                       |
| async_tree_io_tg           | 669 ms                                                 | 695 ms: 1.04x slower                                       |
| async_tree_memoization_tg  | 323 ms                                                 | 336 ms: 1.04x slower                                       |
| async_tree_none_tg         | 258 ms                                                 | 270 ms: 1.05x slower                                       |
| async_tree_io              | 668 ms                                                 | 710 ms: 1.06x slower                                       |
| async_tree_memoization     | 312 ms                                                 | 333 ms: 1.07x slower                                       |
| Geometric mean             | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                       |
| float          | 55.8 ms                                                | 56.5 ms: 1.01x slower                                      |
| nbody          | 68.8 ms                                                | 71.5 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 74.6 ms: 1.04x faster                                      |
| regex_effbot   | 2.64 ms                                                | 2.63 ms: 1.01x faster                                      |
| regex_dna      | 154 ms                                                 | 158 ms: 1.02x slower                                       |
| regex_v8       | 16.0 ms                                                | 17.3 ms: 1.08x slower                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| json_loads           | 17.2 us                                                | 16.8 us: 1.03x faster                                      |
| xml_etree_process    | 39.7 ms                                                | 39.3 ms: 1.01x faster                                      |
| unpickle_list        | 3.02 us                                                | 2.99 us: 1.01x faster                                      |
| unpickle             | 9.12 us                                                | 9.04 us: 1.01x faster                                      |
| xml_etree_generate   | 55.8 ms                                                | 56.0 ms: 1.00x slower                                      |
| pickle               | 7.23 us                                                | 7.34 us: 1.02x slower                                      |
| pickle_list          | 2.89 us                                                | 2.94 us: 1.02x slower                                      |
| xml_etree_parse      | 106 ms                                                 | 109 ms: 1.03x slower                                       |
| xml_etree_iterparse  | 74.0 ms                                                | 76.3 ms: 1.03x slower                                      |
| unpickle_pure_python | 151 us                                                 | 155 us: 1.03x slower                                       |
| json_dumps           | 6.22 ms                                                | 6.54 ms: 1.05x slower                                      |
| tomli_loads          | 1.39 sec                                               | 1.53 sec: 1.10x slower                                     |
| Geometric mean       | (ref)                                                  | 1.02x slower                                               |

Benchmark hidden because not significant (2): pickle_dict, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 16.6 ms: 1.45x slower                                      |
| python_startup_no_site | 9.37 ms                                                | 14.7 ms: 1.57x slower                                      |
| Geometric mean         | (ref)                                                  | 1.51x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 7.71 ms                                                | 7.35 ms: 1.05x faster                                      |
| django_template | 22.3 ms                                                | 21.5 ms: 1.04x faster                                      |
| Geometric mean  | (ref)                                                  | 1.04x faster                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| comprehensions             | 14.5 us                                                | 11.3 us: 1.29x faster                                      |
| typing_runtime_protocols   | 93.0 us                                                | 73.2 us: 1.27x faster                                      |
| raytrace                   | 212 ms                                                 | 179 ms: 1.18x faster                                       |
| unpack_sequence            | 31.5 ns                                                | 27.7 ns: 1.14x faster                                      |
| generators                 | 31.1 ms                                                | 28.0 ms: 1.11x faster                                      |
| deltablue                  | 2.71 ms                                                | 2.44 ms: 1.11x faster                                      |
| deepcopy_memo              | 27.7 us                                                | 25.3 us: 1.09x faster                                      |
| logging_silent             | 76.4 ns                                                | 70.6 ns: 1.08x faster                                      |
| crypto_pyaes               | 51.9 ms                                                | 47.9 ms: 1.08x faster                                      |
| sympy_str                  | 148 ms                                                 | 136 ms: 1.08x faster                                       |
| sympy_sum                  | 77.6 ms                                                | 72.0 ms: 1.08x faster                                      |
| sympy_integrate            | 11.4 ms                                                | 10.5 ms: 1.08x faster                                      |
| deepcopy_reduce            | 2.07 us                                                | 1.92 us: 1.08x faster                                      |
| nqueens                    | 62.4 ms                                                | 58.1 ms: 1.07x faster                                      |
| deepcopy                   | 235 us                                                 | 221 us: 1.06x faster                                       |
| coroutines                 | 19.2 ms                                                | 18.2 ms: 1.05x faster                                      |
| sqlglot_parse              | 848 us                                                 | 805 us: 1.05x faster                                       |
| mako                       | 7.71 ms                                                | 7.35 ms: 1.05x faster                                      |
| regex_compile              | 77.9 ms                                                | 74.6 ms: 1.04x faster                                      |
| logging_format             | 3.98 us                                                | 3.82 us: 1.04x faster                                      |
| scimark_lu                 | 76.0 ms                                                | 72.8 ms: 1.04x faster                                      |
| logging_simple             | 3.69 us                                                | 3.53 us: 1.04x faster                                      |
| sqlglot_transpile          | 1.02 ms                                                | 980 us: 1.04x faster                                       |
| json                       | 3.09 ms                                                | 2.97 ms: 1.04x faster                                      |
| django_template            | 22.3 ms                                                | 21.5 ms: 1.04x faster                                      |
| sympy_expand               | 241 ms                                                 | 232 ms: 1.04x faster                                       |
| async_tree_none            | 266 ms                                                 | 256 ms: 1.04x faster                                       |
| sqlglot_normalize          | 186 ms                                                 | 180 ms: 1.03x faster                                       |
| docutils                   | 1.50 sec                                               | 1.45 sec: 1.03x faster                                     |
| bench_thread_pool          | 504 us                                                 | 488 us: 1.03x faster                                       |
| chaos                      | 42.5 ms                                                | 41.2 ms: 1.03x faster                                      |
| spectral_norm              | 76.4 ms                                                | 74.0 ms: 1.03x faster                                      |
| json_loads                 | 17.2 us                                                | 16.8 us: 1.03x faster                                      |
| sqlglot_optimize           | 34.0 ms                                                | 33.3 ms: 1.02x faster                                      |
| dulwich_log                | 29.8 ms                                                | 29.2 ms: 1.02x faster                                      |
| async_generators           | 304 ms                                                 | 299 ms: 1.02x faster                                       |
| mdp                        | 1.58 sec                                               | 1.56 sec: 1.01x faster                                     |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.10 ms: 1.01x faster                                      |
| xml_etree_process          | 39.7 ms                                                | 39.3 ms: 1.01x faster                                      |
| unpickle_list              | 3.02 us                                                | 2.99 us: 1.01x faster                                      |
| unpickle                   | 9.12 us                                                | 9.04 us: 1.01x faster                                      |
| pprint_pformat             | 1.01 sec                                               | 1.00 sec: 1.01x faster                                     |
| regex_effbot               | 2.64 ms                                                | 2.63 ms: 1.01x faster                                      |
| pprint_safe_repr           | 497 ms                                                 | 495 ms: 1.01x faster                                       |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                       |
| xml_etree_generate         | 55.8 ms                                                | 56.0 ms: 1.00x slower                                      |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                       |
| gc_traversal               | 2.40 ms                                                | 2.41 ms: 1.00x slower                                      |
| create_gc_cycles           | 701 us                                                 | 705 us: 1.00x slower                                       |
| chameleon                  | 4.70 ms                                                | 4.75 ms: 1.01x slower                                      |
| float                      | 55.8 ms                                                | 56.5 ms: 1.01x slower                                      |
| meteor_contest             | 71.7 ms                                                | 72.9 ms: 1.02x slower                                      |
| pickle                     | 7.23 us                                                | 7.34 us: 1.02x slower                                      |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 542 ms: 1.02x slower                                       |
| pickle_list                | 2.89 us                                                | 2.94 us: 1.02x slower                                      |
| sqlite_synth               | 1.57 us                                                | 1.60 us: 1.02x slower                                      |
| pycparser                  | 677 ms                                                 | 692 ms: 1.02x slower                                       |
| regex_dna                  | 154 ms                                                 | 158 ms: 1.02x slower                                       |
| xml_etree_parse            | 106 ms                                                 | 109 ms: 1.03x slower                                       |
| scimark_fft                | 195 ms                                                 | 201 ms: 1.03x slower                                       |
| xml_etree_iterparse        | 74.0 ms                                                | 76.3 ms: 1.03x slower                                      |
| unpickle_pure_python       | 151 us                                                 | 155 us: 1.03x slower                                       |
| go                         | 102 ms                                                 | 105 ms: 1.03x slower                                       |
| scimark_monte_carlo        | 45.0 ms                                                | 46.6 ms: 1.03x slower                                      |
| 2to3                       | 169 ms                                                 | 176 ms: 1.04x slower                                       |
| async_tree_io_tg           | 669 ms                                                 | 695 ms: 1.04x slower                                       |
| nbody                      | 68.8 ms                                                | 71.5 ms: 1.04x slower                                      |
| async_tree_memoization_tg  | 323 ms                                                 | 336 ms: 1.04x slower                                       |
| hexiom                     | 4.54 ms                                                | 4.77 ms: 1.05x slower                                      |
| async_tree_none_tg         | 258 ms                                                 | 270 ms: 1.05x slower                                       |
| json_dumps                 | 6.22 ms                                                | 6.54 ms: 1.05x slower                                      |
| richards_super             | 36.0 ms                                                | 38.2 ms: 1.06x slower                                      |
| pyflate                    | 316 ms                                                 | 335 ms: 1.06x slower                                       |
| async_tree_io              | 668 ms                                                 | 710 ms: 1.06x slower                                       |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.32 sec: 1.06x slower                                     |
| async_tree_memoization     | 312 ms                                                 | 333 ms: 1.07x slower                                       |
| richards                   | 32.1 ms                                                | 34.3 ms: 1.07x slower                                      |
| bench_mp_pool              | 44.9 ms                                                | 48.1 ms: 1.07x slower                                      |
| pathlib                    | 24.2 ms                                                | 26.0 ms: 1.08x slower                                      |
| regex_v8                   | 16.0 ms                                                | 17.3 ms: 1.08x slower                                      |
| fannkuch                   | 248 ms                                                 | 271 ms: 1.09x slower                                       |
| tomli_loads                | 1.39 sec                                               | 1.53 sec: 1.10x slower                                     |
| scimark_sor                | 87.4 ms                                                | 104 ms: 1.19x slower                                       |
| aiohttp                    | 1.08 ms                                                | 1.28 ms: 1.19x slower                                      |
| gunicorn                   | 1.15 ms                                                | 1.38 ms: 1.20x slower                                      |
| coverage                   | 38.9 ms                                                | 47.1 ms: 1.21x slower                                      |
| telco                      | 3.68 ms                                                | 4.47 ms: 1.21x slower                                      |
| tornado_http               | 69.3 ms                                                | 86.2 ms: 1.24x slower                                      |
| python_startup             | 11.4 ms                                                | 16.6 ms: 1.45x slower                                      |
| python_startup_no_site     | 9.37 ms                                                | 14.7 ms: 1.57x slower                                      |
| mypy2                      | 380 ms                                                 | 611 ms: 1.61x slower                                       |
| Geometric mean             | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (4): asyncio_tcp, async_tree_cpu_io_mixed, pickle_dict, pickle_pure_python
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (15) of results/bm-20231122-3.13.0a2-9c4347e-PYTHON_UOPS/bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.011x slower
# HPT report

- Reliability score: 87.28% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.55x