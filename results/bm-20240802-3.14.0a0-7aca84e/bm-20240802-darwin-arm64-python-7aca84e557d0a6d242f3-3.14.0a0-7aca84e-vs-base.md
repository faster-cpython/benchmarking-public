# Results vs. base

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: darwin-arm64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.00x faster
- HPT reliability: 82.01%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240802-darwin-arm64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 163 ms                                                                | 164 ms: 1.01x slower                                                  |
| docutils       | 1.49 sec                                                              | 1.49 sec: 1.00x slower                                                |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark           | bm-20240802-darwin-arm64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|---------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_tcp         | 435 ms                                                                | 405 ms: 1.07x faster                                                  |
| async_tree_eager_tg | 43.2 ms                                                               | 42.2 ms: 1.02x faster                                                 |
| async_tree_eager    | 63.4 ms                                                               | 62.3 ms: 1.02x faster                                                 |
| async_generators    | 281 ms                                                                | 280 ms: 1.00x faster                                                  |
| coroutines          | 16.1 ms                                                               | 16.1 ms: 1.00x slower                                                 |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (16): async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_io, async_tree_memoization_tg, asyncio_websockets, async_tree_eager_cpu_io_mixed, async_tree_eager_io_tg, async_tree_none_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed, async_tree_io_tg, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240802-darwin-arm64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 60.3 ms                                                               | 59.6 ms: 1.01x faster                                                 |
| float          | 48.5 ms                                                               | 48.4 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240802-darwin-arm64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 68.2 ms                                                               | 68.4 ms: 1.00x slower                                                 |
| regex_effbot   | 2.54 ms                                                               | 2.55 ms: 1.00x slower                                                 |
| regex_v8       | 17.3 ms                                                               | 17.4 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240802-darwin-arm64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|--------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads        | 1.50 sec                                                              | 1.48 sec: 1.01x faster                                                |
| json_loads         | 17.2 us                                                               | 17.2 us: 1.00x faster                                                 |
| xml_etree_process  | 37.7 ms                                                               | 37.9 ms: 1.00x slower                                                 |
| pickle_pure_python | 183 us                                                                | 184 us: 1.01x slower                                                  |
| json_dumps         | 6.39 ms                                                               | 6.54 ms: 1.02x slower                                                 |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (4): xml_etree_generate, unpickle_pure_python, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240802-darwin-arm64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 16.4 ms                                                               | 15.4 ms: 1.06x faster                                                 |
| python_startup_no_site | 13.3 ms                                                               | 12.8 ms: 1.04x faster                                                 |
| Geometric mean         | (ref)                                                                 | 1.05x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240802-darwin-arm64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.16 ms                                                               | 7.02 ms: 1.02x faster                                                 |
| django_template | 19.7 ms                                                               | 19.9 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240802-darwin-arm64-python-498376d7a7d6f704f22a-3.14.0a0-498376d | bm-20240802-darwin-arm64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| asyncio_tcp              | 435 ms                                                                | 405 ms: 1.07x faster                                                  |
| python_startup           | 16.4 ms                                                               | 15.4 ms: 1.06x faster                                                 |
| python_startup_no_site   | 13.3 ms                                                               | 12.8 ms: 1.04x faster                                                 |
| async_tree_eager_tg      | 43.2 ms                                                               | 42.2 ms: 1.02x faster                                                 |
| mako                     | 7.16 ms                                                               | 7.02 ms: 1.02x faster                                                 |
| async_tree_eager         | 63.4 ms                                                               | 62.3 ms: 1.02x faster                                                 |
| scimark_sparse_mat_mult  | 2.81 ms                                                               | 2.77 ms: 1.02x faster                                                 |
| tomli_loads              | 1.50 sec                                                              | 1.48 sec: 1.01x faster                                                |
| bench_mp_pool            | 49.0 ms                                                               | 48.3 ms: 1.01x faster                                                 |
| pathlib                  | 23.4 ms                                                               | 23.1 ms: 1.01x faster                                                 |
| logging_format           | 3.42 us                                                               | 3.38 us: 1.01x faster                                                 |
| scimark_sor              | 94.4 ms                                                               | 93.2 ms: 1.01x faster                                                 |
| scimark_lu               | 67.9 ms                                                               | 67.0 ms: 1.01x faster                                                 |
| hexiom                   | 4.10 ms                                                               | 4.06 ms: 1.01x faster                                                 |
| nbody                    | 60.3 ms                                                               | 59.6 ms: 1.01x faster                                                 |
| fannkuch                 | 265 ms                                                                | 263 ms: 1.01x faster                                                  |
| mdp                      | 1.43 sec                                                              | 1.42 sec: 1.01x faster                                                |
| scimark_fft              | 186 ms                                                                | 185 ms: 1.01x faster                                                  |
| logging_simple           | 3.07 us                                                               | 3.05 us: 1.01x faster                                                 |
| json_loads               | 17.2 us                                                               | 17.2 us: 1.00x faster                                                 |
| nqueens                  | 53.6 ms                                                               | 53.3 ms: 1.00x faster                                                 |
| float                    | 48.5 ms                                                               | 48.4 ms: 1.00x faster                                                 |
| async_generators         | 281 ms                                                                | 280 ms: 1.00x faster                                                  |
| bpe_tokeniser            | 3.11 sec                                                              | 3.10 sec: 1.00x faster                                                |
| deltablue                | 2.11 ms                                                               | 2.12 ms: 1.00x slower                                                 |
| sympy_str                | 134 ms                                                                | 135 ms: 1.00x slower                                                  |
| logging_silent           | 59.8 ns                                                               | 60.0 ns: 1.00x slower                                                 |
| regex_compile            | 68.2 ms                                                               | 68.4 ms: 1.00x slower                                                 |
| regex_effbot             | 2.54 ms                                                               | 2.55 ms: 1.00x slower                                                 |
| raytrace                 | 148 ms                                                                | 148 ms: 1.00x slower                                                  |
| docutils                 | 1.49 sec                                                              | 1.49 sec: 1.00x slower                                                |
| meteor_contest           | 71.8 ms                                                               | 72.1 ms: 1.00x slower                                                 |
| richards_super           | 34.4 ms                                                               | 34.6 ms: 1.00x slower                                                 |
| coroutines               | 16.1 ms                                                               | 16.1 ms: 1.00x slower                                                 |
| xml_etree_process        | 37.7 ms                                                               | 37.9 ms: 1.00x slower                                                 |
| deepcopy_reduce          | 1.49 us                                                               | 1.50 us: 1.01x slower                                                 |
| pickle_pure_python       | 183 us                                                                | 184 us: 1.01x slower                                                  |
| 2to3                     | 163 ms                                                                | 164 ms: 1.01x slower                                                  |
| pprint_safe_repr         | 467 ms                                                                | 470 ms: 1.01x slower                                                  |
| sympy_integrate          | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                 |
| regex_v8                 | 17.3 ms                                                               | 17.4 ms: 1.01x slower                                                 |
| deepcopy                 | 144 us                                                                | 145 us: 1.01x slower                                                  |
| sympy_sum                | 70.5 ms                                                               | 71.0 ms: 1.01x slower                                                 |
| sqlglot_optimize         | 31.4 ms                                                               | 31.6 ms: 1.01x slower                                                 |
| pprint_pformat           | 951 ms                                                                | 958 ms: 1.01x slower                                                  |
| chaos                    | 35.6 ms                                                               | 36.0 ms: 1.01x slower                                                 |
| sympy_expand             | 229 ms                                                                | 232 ms: 1.01x slower                                                  |
| richards                 | 31.3 ms                                                               | 31.6 ms: 1.01x slower                                                 |
| sqlglot_normalize        | 169 ms                                                                | 171 ms: 1.01x slower                                                  |
| django_template          | 19.7 ms                                                               | 19.9 ms: 1.01x slower                                                 |
| json_dumps               | 6.39 ms                                                               | 6.54 ms: 1.02x slower                                                 |
| typing_runtime_protocols | 91.9 us                                                               | 94.2 us: 1.03x slower                                                 |
| comprehensions           | 10.2 us                                                               | 10.9 us: 1.07x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (46): async_tree_eager_memoization, json, bench_thread_pool, crypto_pyaes, async_tree_eager_memoization_tg, spectral_norm, async_tree_eager_io, async_tree_memoization_tg, asyncio_websockets, regex_dna, pyflate, genshi_text, create_gc_cycles, async_tree_eager_cpu_io_mixed, telco, thrift, scimark_monte_carlo, tornado_http, generators, xml_etree_generate, async_tree_eager_io_tg, async_tree_none_tg, pidigits, async_tree_eager_cpu_io_mixed_tg, async_tree_io, dulwich_log, async_tree_cpu_io_mixed_tg, deepcopy_memo, sqlglot_parse, go, async_tree_memoization, html5lib, dask, unpickle_pure_python, coverage, async_tree_none, xml_etree_iterparse, genshi_xml, async_tree_cpu_io_mixed, sqlglot_transpile, async_tree_io_tg, xml_etree_parse, asyncio_tcp_ssl, gc_traversal, pycparser, pylint

# HPT report

- Reliability score: 82.01% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x