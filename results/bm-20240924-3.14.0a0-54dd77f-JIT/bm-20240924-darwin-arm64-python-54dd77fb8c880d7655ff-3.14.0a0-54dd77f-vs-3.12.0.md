# Results vs. 3.12.0

- fork: python
- ref: 54dd77fb8c880d7655ff
- machine: darwin-arm64
- commit hash: 54dd77f
- commit date: 2024-09-24
- overall geometric mean: 1.045x faster
- HPT reliability: 98.61%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.68x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 176 ms: 1.04x slower                                                  |
| docutils       | 1.50 sec                                               | 1.56 sec: 1.04x slower                                                |
| tornado_http   | 69.3 ms                                                | 81.7 ms: 1.18x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 188 ms: 1.37x faster                                                  |
| async_tree_none            | 266 ms                                                 | 201 ms: 1.32x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 249 ms: 1.25x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 258 ms: 1.25x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 547 ms: 1.22x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 464 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 461 ms: 1.14x faster                                                  |
| async_tree_io              | 668 ms                                                 | 592 ms: 1.13x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 46.1 ms: 1.21x faster                                                 |
| nbody          | 68.8 ms                                                | 63.5 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.46 ms: 1.07x faster                                                 |
| regex_dna      | 154 ms                                                 | 145 ms: 1.07x faster                                                  |
| regex_compile  | 77.9 ms                                                | 75.6 ms: 1.03x faster                                                 |
| regex_v8       | 16.0 ms                                                | 16.5 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_process    | 39.7 ms                                                | 34.3 ms: 1.16x faster                                                 |
| unpickle_pure_python | 151 us                                                 | 131 us: 1.15x faster                                                  |
| tomli_loads          | 1.39 sec                                               | 1.24 sec: 1.12x faster                                                |
| pickle_pure_python   | 200 us                                                 | 179 us: 1.12x faster                                                  |
| xml_etree_generate   | 55.8 ms                                                | 51.1 ms: 1.09x faster                                                 |
| unpickle_list        | 3.02 us                                                | 2.89 us: 1.04x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 71.7 ms: 1.03x faster                                                 |
| json_loads           | 17.2 us                                                | 16.8 us: 1.02x faster                                                 |
| json_dumps           | 6.22 ms                                                | 6.17 ms: 1.01x faster                                                 |
| unpickle             | 9.12 us                                                | 9.28 us: 1.02x slower                                                 |
| pickle_dict          | 18.1 us                                                | 18.5 us: 1.03x slower                                                 |
| pickle_list          | 2.89 us                                                | 2.98 us: 1.03x slower                                                 |
| pickle               | 7.23 us                                                | 7.47 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.8 ms: 1.47x slower                                                 |
| python_startup         | 11.4 ms                                                | 16.9 ms: 1.48x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.47x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.47 ms: 1.19x faster                                                 |
| django_template | 22.3 ms                                                | 22.8 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.0 us: 1.73x faster                                                 |
| deepcopy                   | 235 us                                                 | 152 us: 1.54x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.51 us: 1.37x faster                                                 |
| async_tree_none_tg         | 258 ms                                                 | 188 ms: 1.37x faster                                                  |
| async_tree_none            | 266 ms                                                 | 201 ms: 1.32x faster                                                  |
| generators                 | 31.1 ms                                                | 24.4 ms: 1.27x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 249 ms: 1.25x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 258 ms: 1.25x faster                                                  |
| raytrace                   | 212 ms                                                 | 173 ms: 1.23x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 547 ms: 1.22x faster                                                  |
| logging_silent             | 76.4 ns                                                | 62.5 ns: 1.22x faster                                                 |
| logging_simple             | 3.69 us                                                | 3.02 us: 1.22x faster                                                 |
| float                      | 55.8 ms                                                | 46.1 ms: 1.21x faster                                                 |
| logging_format             | 3.98 us                                                | 3.31 us: 1.20x faster                                                 |
| mako                       | 7.71 ms                                                | 6.47 ms: 1.19x faster                                                 |
| scimark_lu                 | 76.0 ms                                                | 63.9 ms: 1.19x faster                                                 |
| coroutines                 | 19.2 ms                                                | 16.4 ms: 1.17x faster                                                 |
| xml_etree_process          | 39.7 ms                                                | 34.3 ms: 1.16x faster                                                 |
| unpickle_pure_python       | 151 us                                                 | 131 us: 1.15x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.36 ms: 1.15x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 464 ms: 1.15x faster                                                  |
| spectral_norm              | 76.4 ms                                                | 66.7 ms: 1.15x faster                                                 |
| comprehensions             | 14.5 us                                                | 12.7 us: 1.14x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 461 ms: 1.14x faster                                                  |
| async_tree_io              | 668 ms                                                 | 592 ms: 1.13x faster                                                  |
| tomli_loads                | 1.39 sec                                               | 1.24 sec: 1.12x faster                                                |
| pickle_pure_python         | 200 us                                                 | 179 us: 1.12x faster                                                  |
| mdp                        | 1.58 sec                                               | 1.44 sec: 1.10x faster                                                |
| xml_etree_generate         | 55.8 ms                                                | 51.1 ms: 1.09x faster                                                 |
| nbody                      | 68.8 ms                                                | 63.5 ms: 1.08x faster                                                 |
| nqueens                    | 62.4 ms                                                | 57.9 ms: 1.08x faster                                                 |
| bench_thread_pool          | 504 us                                                 | 470 us: 1.07x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.46 ms: 1.07x faster                                                 |
| asyncio_tcp                | 449 ms                                                 | 420 ms: 1.07x faster                                                  |
| regex_dna                  | 154 ms                                                 | 145 ms: 1.07x faster                                                  |
| chaos                      | 42.5 ms                                                | 39.9 ms: 1.07x faster                                                 |
| json                       | 3.09 ms                                                | 2.90 ms: 1.06x faster                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.96 ms: 1.06x faster                                                 |
| scimark_fft                | 195 ms                                                 | 185 ms: 1.05x faster                                                  |
| unpickle_list              | 3.02 us                                                | 2.89 us: 1.04x faster                                                 |
| async_generators           | 304 ms                                                 | 292 ms: 1.04x faster                                                  |
| sqlglot_normalize          | 186 ms                                                 | 180 ms: 1.03x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 71.7 ms: 1.03x faster                                                 |
| regex_compile              | 77.9 ms                                                | 75.6 ms: 1.03x faster                                                 |
| dulwich_log                | 29.8 ms                                                | 29.0 ms: 1.03x faster                                                 |
| sympy_str                  | 148 ms                                                 | 144 ms: 1.03x faster                                                  |
| pathlib                    | 24.2 ms                                                | 23.6 ms: 1.03x faster                                                 |
| sympy_sum                  | 77.6 ms                                                | 75.8 ms: 1.02x faster                                                 |
| json_loads                 | 17.2 us                                                | 16.8 us: 1.02x faster                                                 |
| go                         | 102 ms                                                 | 100 ms: 1.01x faster                                                  |
| json_dumps                 | 6.22 ms                                                | 6.17 ms: 1.01x faster                                                 |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                  |
| sqlite_synth               | 1.57 us                                                | 1.58 us: 1.00x slower                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 93.6 us: 1.01x slower                                                 |
| sqlglot_parse              | 848 us                                                 | 855 us: 1.01x slower                                                  |
| pycparser                  | 677 ms                                                 | 685 ms: 1.01x slower                                                  |
| pprint_safe_repr           | 497 ms                                                 | 504 ms: 1.01x slower                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 1.04 ms: 1.02x slower                                                 |
| sympy_integrate            | 11.4 ms                                                | 11.6 ms: 1.02x slower                                                 |
| unpickle                   | 9.12 us                                                | 9.28 us: 1.02x slower                                                 |
| django_template            | 22.3 ms                                                | 22.8 ms: 1.02x slower                                                 |
| pprint_pformat             | 1.01 sec                                               | 1.03 sec: 1.02x slower                                                |
| pickle_dict                | 18.1 us                                                | 18.5 us: 1.03x slower                                                 |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.03x slower                                                 |
| sympy_expand               | 241 ms                                                 | 248 ms: 1.03x slower                                                  |
| pickle_list                | 2.89 us                                                | 2.98 us: 1.03x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 16.5 ms: 1.03x slower                                                 |
| pickle                     | 7.23 us                                                | 7.47 us: 1.03x slower                                                 |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.29 sec: 1.03x slower                                                |
| pyflate                    | 316 ms                                                 | 327 ms: 1.04x slower                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 35.3 ms: 1.04x slower                                                 |
| 2to3                       | 169 ms                                                 | 176 ms: 1.04x slower                                                  |
| docutils                   | 1.50 sec                                               | 1.56 sec: 1.04x slower                                                |
| hexiom                     | 4.54 ms                                                | 4.73 ms: 1.04x slower                                                 |
| meteor_contest             | 71.7 ms                                                | 74.9 ms: 1.04x slower                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 48.0 ms: 1.07x slower                                                 |
| fannkuch                   | 248 ms                                                 | 269 ms: 1.08x slower                                                  |
| coverage                   | 38.9 ms                                                | 44.4 ms: 1.14x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 51.6 ms: 1.15x slower                                                 |
| tornado_http               | 69.3 ms                                                | 81.7 ms: 1.18x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 905 us: 1.29x slower                                                  |
| telco                      | 3.68 ms                                                | 4.78 ms: 1.30x slower                                                 |
| richards_super             | 36.0 ms                                                | 47.9 ms: 1.33x slower                                                 |
| richards                   | 32.1 ms                                                | 45.9 ms: 1.43x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 13.8 ms: 1.47x slower                                                 |
| python_startup             | 11.4 ms                                                | 16.9 ms: 1.48x slower                                                 |
| unpack_sequence            | 31.5 ns                                                | 76.0 ns: 2.42x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                          |

Benchmark hidden because not significant (4): xml_etree_parse, scimark_sor, pidigits, crypto_pyaes
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (14) of results/bm-20240924-3.14.0a0-54dd77f-JIT/bm-20240924-darwin-arm64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.045x faster
# HPT report

- Reliability score: 98.61% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.68x