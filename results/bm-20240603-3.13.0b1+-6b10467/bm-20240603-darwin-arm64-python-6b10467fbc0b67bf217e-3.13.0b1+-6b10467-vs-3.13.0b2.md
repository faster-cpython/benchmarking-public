# Results vs. 3.13.0b2

- fork: python
- ref: 6b10467fbc0b67bf217e
- machine: darwin-arm64
- commit hash: 6b10467
- commit date: 2024-06-03
- overall geometric mean: 1.00x faster
- HPT reliability: 95.41%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-darwin-arm64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 1.44 sec                                                   | 1.43 sec: 1.00x faster                                                 |
| html5lib       | 31.2 ms                                                    | 31.3 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                      | 1.00x faster                                                           |

Benchmark hidden because not significant (3): 2to3, chameleon, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark           | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-darwin-arm64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|---------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager_tg | 41.4 ms                                                    | 41.6 ms: 1.01x slower                                                  |
| async_tree_eager    | 60.3 ms                                                    | 61.7 ms: 1.02x slower                                                  |
| Geometric mean      | (ref)                                                      | 1.01x faster                                                           |

Benchmark hidden because not significant (14): async_tree_eager_io_tg, async_tree_eager_io, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg, async_tree_eager_memoization, async_tree_none, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-darwin-arm64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 59.6 ms                                                    | 60.8 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                      | 1.01x slower                                                           |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-darwin-arm64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 68.5 ms                                                    | 68.2 ms: 1.00x faster                                                  |
| regex_effbot   | 2.58 ms                                                    | 2.59 ms: 1.00x slower                                                  |
| regex_v8       | 17.3 ms                                                    | 17.3 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                      | 1.00x slower                                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-darwin-arm64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                     | 102 ms: 1.03x faster                                                   |
| tomli_loads          | 1.47 sec                                                   | 1.45 sec: 1.01x faster                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 52.1 ms: 1.01x faster                                                  |
| json_loads           | 16.8 us                                                    | 16.9 us: 1.00x slower                                                  |
| pickle_pure_python   | 179 us                                                     | 179 us: 1.00x slower                                                   |
| unpickle_list        | 2.88 us                                                    | 2.90 us: 1.01x slower                                                  |
| unpickle_pure_python | 141 us                                                     | 142 us: 1.01x slower                                                   |
| unpickle             | 9.12 us                                                    | 9.23 us: 1.01x slower                                                  |
| json_dumps           | 6.23 ms                                                    | 6.36 ms: 1.02x slower                                                  |
| pickle_list          | 2.96 us                                                    | 3.02 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.00x slower                                                           |

Benchmark hidden because not significant (4): xml_etree_iterparse, pickle, pickle_dict, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-darwin-arm64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 10.8 ms: 1.14x faster                                                  |
| python_startup         | 15.2 ms                                                    | 13.8 ms: 1.10x faster                                                  |
| Geometric mean         | (ref)                                                      | 1.12x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-darwin-arm64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 29.9 ms                                                    | 29.7 ms: 1.01x faster                                                  |
| mako            | 6.99 ms                                                    | 6.94 ms: 1.01x faster                                                  |
| django_template | 19.4 ms                                                    | 19.3 ms: 1.00x faster                                                  |
| Geometric mean  | (ref)                                                      | 1.00x faster                                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-darwin-arm64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|--------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| flaskblogging            | 3.61 ms                                                    | 3.11 ms: 1.16x faster                                                  |
| python_startup_no_site   | 12.3 ms                                                    | 10.8 ms: 1.14x faster                                                  |
| python_startup           | 15.2 ms                                                    | 13.8 ms: 1.10x faster                                                  |
| pathlib                  | 23.3 ms                                                    | 22.1 ms: 1.06x faster                                                  |
| asyncio_tcp_ssl          | 1.29 sec                                                   | 1.23 sec: 1.05x faster                                                 |
| xml_etree_parse          | 106 ms                                                     | 102 ms: 1.03x faster                                                   |
| bench_mp_pool            | 47.2 ms                                                    | 46.0 ms: 1.03x faster                                                  |
| dask                     | 221 ms                                                     | 217 ms: 1.02x faster                                                   |
| telco                    | 4.60 ms                                                    | 4.53 ms: 1.02x faster                                                  |
| tomli_loads              | 1.47 sec                                                   | 1.45 sec: 1.01x faster                                                 |
| deepcopy_reduce          | 1.82 us                                                    | 1.80 us: 1.01x faster                                                  |
| sqlite_synth             | 1.55 us                                                    | 1.53 us: 1.01x faster                                                  |
| xml_etree_generate       | 52.7 ms                                                    | 52.1 ms: 1.01x faster                                                  |
| pyflate                  | 321 ms                                                     | 318 ms: 1.01x faster                                                   |
| generators               | 22.9 ms                                                    | 22.7 ms: 1.01x faster                                                  |
| richards_super           | 35.2 ms                                                    | 35.0 ms: 1.01x faster                                                  |
| genshi_xml               | 29.9 ms                                                    | 29.7 ms: 1.01x faster                                                  |
| dulwich_log              | 27.6 ms                                                    | 27.4 ms: 1.01x faster                                                  |
| mako                     | 6.99 ms                                                    | 6.94 ms: 1.01x faster                                                  |
| pprint_pformat           | 947 ms                                                     | 941 ms: 1.01x faster                                                   |
| create_gc_cycles         | 897 us                                                     | 892 us: 1.01x faster                                                   |
| scimark_lu               | 66.9 ms                                                    | 66.6 ms: 1.00x faster                                                  |
| django_template          | 19.4 ms                                                    | 19.3 ms: 1.00x faster                                                  |
| docutils                 | 1.44 sec                                                   | 1.43 sec: 1.00x faster                                                 |
| regex_compile            | 68.5 ms                                                    | 68.2 ms: 1.00x faster                                                  |
| pprint_safe_repr         | 465 ms                                                     | 463 ms: 1.00x faster                                                   |
| meteor_contest           | 70.3 ms                                                    | 70.1 ms: 1.00x faster                                                  |
| regex_effbot             | 2.58 ms                                                    | 2.59 ms: 1.00x slower                                                  |
| sympy_str                | 131 ms                                                     | 132 ms: 1.00x slower                                                   |
| json_loads               | 16.8 us                                                    | 16.9 us: 1.00x slower                                                  |
| deltablue                | 2.14 ms                                                    | 2.15 ms: 1.00x slower                                                  |
| scimark_monte_carlo      | 42.5 ms                                                    | 42.6 ms: 1.00x slower                                                  |
| pickle_pure_python       | 179 us                                                     | 179 us: 1.00x slower                                                   |
| regex_v8                 | 17.3 ms                                                    | 17.3 ms: 1.00x slower                                                  |
| spectral_norm            | 66.4 ms                                                    | 66.6 ms: 1.00x slower                                                  |
| thrift                   | 435 us                                                     | 437 us: 1.00x slower                                                   |
| sqlglot_optimize         | 30.9 ms                                                    | 31.0 ms: 1.00x slower                                                  |
| async_tree_eager_tg      | 41.4 ms                                                    | 41.6 ms: 1.01x slower                                                  |
| html5lib                 | 31.2 ms                                                    | 31.3 ms: 1.01x slower                                                  |
| sqlglot_parse            | 732 us                                                     | 736 us: 1.01x slower                                                   |
| sqlglot_transpile        | 891 us                                                     | 896 us: 1.01x slower                                                   |
| mdp                      | 1.53 sec                                                   | 1.54 sec: 1.01x slower                                                 |
| scimark_fft              | 181 ms                                                     | 182 ms: 1.01x slower                                                   |
| hexiom                   | 4.06 ms                                                    | 4.09 ms: 1.01x slower                                                  |
| unpickle_list            | 2.88 us                                                    | 2.90 us: 1.01x slower                                                  |
| sqlglot_normalize        | 166 ms                                                     | 167 ms: 1.01x slower                                                   |
| unpickle_pure_python     | 141 us                                                     | 142 us: 1.01x slower                                                   |
| raytrace                 | 147 ms                                                     | 148 ms: 1.01x slower                                                   |
| logging_simple           | 3.04 us                                                    | 3.07 us: 1.01x slower                                                  |
| pycparser                | 632 ms                                                     | 639 ms: 1.01x slower                                                   |
| coroutines               | 15.8 ms                                                    | 16.0 ms: 1.01x slower                                                  |
| crypto_pyaes             | 49.5 ms                                                    | 50.0 ms: 1.01x slower                                                  |
| nqueens                  | 52.2 ms                                                    | 52.8 ms: 1.01x slower                                                  |
| unpickle                 | 9.12 us                                                    | 9.23 us: 1.01x slower                                                  |
| logging_format           | 3.31 us                                                    | 3.36 us: 1.02x slower                                                  |
| chaos                    | 34.0 ms                                                    | 34.6 ms: 1.02x slower                                                  |
| nbody                    | 59.6 ms                                                    | 60.8 ms: 1.02x slower                                                  |
| json_dumps               | 6.23 ms                                                    | 6.36 ms: 1.02x slower                                                  |
| async_tree_eager         | 60.3 ms                                                    | 61.7 ms: 1.02x slower                                                  |
| pickle_list              | 2.96 us                                                    | 3.02 us: 1.02x slower                                                  |
| logging_silent           | 60.1 ns                                                    | 61.6 ns: 1.02x slower                                                  |
| bench_thread_pool        | 447 us                                                     | 460 us: 1.03x slower                                                   |
| typing_runtime_protocols | 87.6 us                                                    | 91.0 us: 1.04x slower                                                  |
| gunicorn                 | 1.04 ms                                                    | 1.08 ms: 1.04x slower                                                  |
| comprehensions           | 10.2 us                                                    | 10.9 us: 1.07x slower                                                  |
| Geometric mean           | (ref)                                                      | 1.00x faster                                                           |

Benchmark hidden because not significant (44): async_tree_eager_io_tg, async_tree_eager_io, async_tree_io, async_tree_io_tg, tornado_http, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg, pylint, async_tree_eager_memoization, async_tree_none, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg, 2to3, fannkuch, async_tree_cpu_io_mixed_tg, sympy_integrate, coverage, mypy2, go, xml_etree_iterparse, regex_dna, async_tree_eager_cpu_io_mixed, sympy_expand, genshi_text, scimark_sor, async_tree_eager_cpu_io_mixed_tg, deepcopy_memo, pidigits, pickle, pickle_dict, asyncio_websockets, xml_etree_process, gc_traversal, chameleon, deepcopy, richards, json, scimark_sparse_mat_mult, async_generators, float, sympy_sum, aiohttp, asyncio_tcp
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 95.41% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.41x