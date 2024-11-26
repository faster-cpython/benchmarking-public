# Results vs. 3.12.0

- fork: python
- ref: 760872efecb95017db8e
- machine: darwin-arm64
- commit hash: 760872e
- commit date: 2024-10-16
- overall geometric mean: 1.039x faster
- HPT reliability: 99.39%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 183 ms: 1.08x slower                                                   |
| docutils       | 1.50 sec                                               | 1.57 sec: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x slower                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 234 ms: 1.38x faster                                                   |
| async_tree_none            | 266 ms                                                 | 197 ms: 1.35x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 243 ms: 1.28x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 212 ms: 1.21x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 455 ms: 1.16x faster                                                   |
| async_tree_io              | 668 ms                                                 | 579 ms: 1.15x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 468 ms: 1.14x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 610 ms: 1.10x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.3 ms: 1.16x faster                                                  |
| nbody          | 68.8 ms                                                | 65.3 ms: 1.05x faster                                                  |
| pidigits       | 282 ms                                                 | 284 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 148 ms: 1.05x faster                                                   |
| regex_compile  | 77.9 ms                                                | 75.0 ms: 1.04x faster                                                  |
| regex_effbot   | 2.64 ms                                                | 2.60 ms: 1.01x faster                                                  |
| regex_v8       | 16.0 ms                                                | 16.8 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_process    | 39.7 ms                                                | 34.5 ms: 1.15x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 132 us: 1.14x faster                                                   |
| pickle_pure_python   | 200 us                                                 | 178 us: 1.12x faster                                                   |
| tomli_loads          | 1.39 sec                                               | 1.24 sec: 1.12x faster                                                 |
| xml_etree_generate   | 55.8 ms                                                | 50.3 ms: 1.11x faster                                                  |
| json_loads           | 17.2 us                                                | 16.5 us: 1.05x faster                                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 72.5 ms: 1.02x faster                                                  |
| unpickle_list        | 3.02 us                                                | 2.97 us: 1.02x faster                                                  |
| unpickle             | 9.12 us                                                | 9.08 us: 1.00x faster                                                  |
| pickle_dict          | 18.1 us                                                | 18.1 us: 1.00x slower                                                  |
| pickle               | 7.23 us                                                | 7.30 us: 1.01x slower                                                  |
| pickle_list          | 2.89 us                                                | 2.94 us: 1.02x slower                                                  |
| json_dumps           | 6.22 ms                                                | 7.12 ms: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 14.6 ms: 1.55x slower                                                  |
| python_startup         | 11.4 ms                                                | 18.9 ms: 1.65x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.60x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.47 ms: 1.19x faster                                                  |
| django_template | 22.3 ms                                                | 22.6 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 242 ms: 1.69x faster                                                   |
| deepcopy_memo              | 27.7 us                                                | 16.8 us: 1.65x faster                                                  |
| deepcopy                   | 235 us                                                 | 152 us: 1.54x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 234 ms: 1.38x faster                                                   |
| deepcopy_reduce            | 2.07 us                                                | 1.50 us: 1.38x faster                                                  |
| async_tree_none            | 266 ms                                                 | 197 ms: 1.35x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 243 ms: 1.28x faster                                                   |
| raytrace                   | 212 ms                                                 | 167 ms: 1.27x faster                                                   |
| generators                 | 31.1 ms                                                | 25.2 ms: 1.23x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 212 ms: 1.21x faster                                                   |
| mako                       | 7.71 ms                                                | 6.47 ms: 1.19x faster                                                  |
| scimark_lu                 | 76.0 ms                                                | 64.4 ms: 1.18x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.13 us: 1.18x faster                                                  |
| logging_format             | 3.98 us                                                | 3.40 us: 1.17x faster                                                  |
| coroutines                 | 19.2 ms                                                | 16.6 ms: 1.16x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 455 ms: 1.16x faster                                                   |
| float                      | 55.8 ms                                                | 48.3 ms: 1.16x faster                                                  |
| async_tree_io              | 668 ms                                                 | 579 ms: 1.15x faster                                                   |
| xml_etree_process          | 39.7 ms                                                | 34.5 ms: 1.15x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 132 us: 1.14x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 468 ms: 1.14x faster                                                   |
| pickle_pure_python         | 200 us                                                 | 178 us: 1.12x faster                                                   |
| tomli_loads                | 1.39 sec                                               | 1.24 sec: 1.12x faster                                                 |
| deltablue                  | 2.71 ms                                                | 2.43 ms: 1.11x faster                                                  |
| comprehensions             | 14.5 us                                                | 13.0 us: 1.11x faster                                                  |
| xml_etree_generate         | 55.8 ms                                                | 50.3 ms: 1.11x faster                                                  |
| spectral_norm              | 76.4 ms                                                | 69.3 ms: 1.10x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 610 ms: 1.10x faster                                                   |
| logging_silent             | 76.4 ns                                                | 69.9 ns: 1.09x faster                                                  |
| pathlib                    | 24.2 ms                                                | 22.3 ms: 1.09x faster                                                  |
| json                       | 3.09 ms                                                | 2.87 ms: 1.08x faster                                                  |
| nqueens                    | 62.4 ms                                                | 58.4 ms: 1.07x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 472 us: 1.07x faster                                                   |
| nbody                      | 68.8 ms                                                | 65.3 ms: 1.05x faster                                                  |
| regex_dna                  | 154 ms                                                 | 148 ms: 1.05x faster                                                   |
| async_generators           | 304 ms                                                 | 291 ms: 1.05x faster                                                   |
| json_loads                 | 17.2 us                                                | 16.5 us: 1.05x faster                                                  |
| regex_compile              | 77.9 ms                                                | 75.0 ms: 1.04x faster                                                  |
| dulwich_log                | 29.8 ms                                                | 28.7 ms: 1.04x faster                                                  |
| go                         | 102 ms                                                 | 98.0 ms: 1.04x faster                                                  |
| mdp                        | 1.58 sec                                               | 1.54 sec: 1.03x faster                                                 |
| chaos                      | 42.5 ms                                                | 41.4 ms: 1.03x faster                                                  |
| scimark_fft                | 195 ms                                                 | 190 ms: 1.03x faster                                                   |
| sqlite_synth               | 1.57 us                                                | 1.54 us: 1.02x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 72.5 ms: 1.02x faster                                                  |
| sqlglot_normalize          | 186 ms                                                 | 182 ms: 1.02x faster                                                   |
| unpickle_list              | 3.02 us                                                | 2.97 us: 1.02x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.60 ms: 1.01x faster                                                  |
| scimark_sor                | 87.4 ms                                                | 86.2 ms: 1.01x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 998 ms: 1.01x faster                                                   |
| unpickle                   | 9.12 us                                                | 9.08 us: 1.00x faster                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.14 ms: 1.00x slower                                                  |
| pickle_dict                | 18.1 us                                                | 18.1 us: 1.00x slower                                                  |
| pidigits                   | 282 ms                                                 | 284 ms: 1.01x slower                                                   |
| pickle                     | 7.23 us                                                | 7.30 us: 1.01x slower                                                  |
| django_template            | 22.3 ms                                                | 22.6 ms: 1.01x slower                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 45.6 ms: 1.01x slower                                                  |
| sympy_expand               | 241 ms                                                 | 245 ms: 1.01x slower                                                   |
| pickle_list                | 2.89 us                                                | 2.94 us: 1.02x slower                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 94.8 us: 1.02x slower                                                  |
| sympy_str                  | 148 ms                                                 | 151 ms: 1.02x slower                                                   |
| sympy_sum                  | 77.6 ms                                                | 79.7 ms: 1.03x slower                                                  |
| richards_super             | 36.0 ms                                                | 37.1 ms: 1.03x slower                                                  |
| sqlglot_parse              | 848 us                                                 | 875 us: 1.03x slower                                                   |
| pyflate                    | 316 ms                                                 | 326 ms: 1.03x slower                                                   |
| sqlglot_transpile          | 1.02 ms                                                | 1.06 ms: 1.04x slower                                                  |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.29 sec: 1.04x slower                                                 |
| crypto_pyaes               | 51.9 ms                                                | 53.9 ms: 1.04x slower                                                  |
| richards                   | 32.1 ms                                                | 33.4 ms: 1.04x slower                                                  |
| docutils                   | 1.50 sec                                               | 1.57 sec: 1.05x slower                                                 |
| meteor_contest             | 71.7 ms                                                | 75.2 ms: 1.05x slower                                                  |
| regex_v8                   | 16.0 ms                                                | 16.8 ms: 1.06x slower                                                  |
| fannkuch                   | 248 ms                                                 | 264 ms: 1.06x slower                                                   |
| sqlglot_optimize           | 34.0 ms                                                | 36.8 ms: 1.08x slower                                                  |
| 2to3                       | 169 ms                                                 | 183 ms: 1.08x slower                                                   |
| hexiom                     | 4.54 ms                                                | 4.92 ms: 1.08x slower                                                  |
| sympy_integrate            | 11.4 ms                                                | 12.5 ms: 1.10x slower                                                  |
| coverage                   | 38.9 ms                                                | 43.9 ms: 1.13x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 7.12 ms: 1.14x slower                                                  |
| telco                      | 3.68 ms                                                | 4.54 ms: 1.23x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.96 ms: 1.23x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 61.8 ms: 1.38x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 14.6 ms: 1.55x slower                                                  |
| python_startup             | 11.4 ms                                                | 18.9 ms: 1.65x slower                                                  |
| create_gc_cycles           | 701 us                                                 | 1.31 ms: 1.87x slower                                                  |
| unpack_sequence            | 31.5 ns                                                | 76.0 ns: 2.42x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (5): asyncio_tcp, pprint_safe_repr, xml_etree_parse, pycparser, tornado_http
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (15) of results/bm-20241016-3.14.0a1+-760872e-JIT/bm-20241016-darwin-arm64-python-760872efecb95017db8e-3.14.0a1+-760872e.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, sphinx, thrift

- Geometric mean (including insignificant results): 1.039x faster
# HPT report

- Reliability score: 99.39% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.27x