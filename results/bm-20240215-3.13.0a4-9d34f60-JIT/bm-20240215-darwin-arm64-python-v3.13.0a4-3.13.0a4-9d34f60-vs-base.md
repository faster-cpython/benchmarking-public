# Results vs. base

- fork: python
- ref: v3.13.0a4
- machine: darwin-arm64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.004x slower
- HPT reliability: 89.38%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| 2to3           | 174 ms                                                                                               | 190 ms: 1.09x slower                                                                                     |
| chameleon      | 4.84 ms                                                                                              | 4.81 ms: 1.01x faster                                                                                    |
| docutils       | 1.46 sec                                                                                             | 1.48 sec: 1.01x slower                                                                                   |
| tornado_http   | 84.4 ms                                                                                              | 69.6 ms: 1.21x faster                                                                                    |
| Geometric mean | (ref)                                                                                                | 1.02x faster                                                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|--------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| coroutines         | 19.2 ms                                                                                              | 18.7 ms: 1.02x faster                                                                                    |
| async_tree_io      | 707 ms                                                                                               | 699 ms: 1.01x faster                                                                                     |
| async_tree_io_tg   | 672 ms                                                                                               | 666 ms: 1.01x faster                                                                                     |
| async_tree_none_tg | 260 ms                                                                                               | 259 ms: 1.01x faster                                                                                     |
| asyncio_websockets | 408 ms                                                                                               | 409 ms: 1.00x slower                                                                                     |
| async_generators   | 297 ms                                                                                               | 303 ms: 1.02x slower                                                                                     |
| Geometric mean     | (ref)                                                                                                | 1.01x faster                                                                                             |

Benchmark hidden because not significant (7): asyncio_tcp_ssl, asyncio_tcp, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| float          | 56.7 ms                                                                                              | 55.5 ms: 1.02x faster                                                                                    |
| nbody          | 74.0 ms                                                                                              | 75.9 ms: 1.03x slower                                                                                    |
| Geometric mean | (ref)                                                                                                | 1.00x slower                                                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| regex_v8       | 17.1 ms                                                                                              | 17.4 ms: 1.02x slower                                                                                    |
| regex_effbot   | 2.49 ms                                                                                              | 2.54 ms: 1.02x slower                                                                                    |
| regex_compile  | 73.4 ms                                                                                              | 75.1 ms: 1.02x slower                                                                                    |
| regex_dna      | 146 ms                                                                                               | 150 ms: 1.03x slower                                                                                     |
| Geometric mean | (ref)                                                                                                | 1.02x slower                                                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|----------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.54 sec                                                                                             | 1.40 sec: 1.10x faster                                                                                   |
| xml_etree_iterparse  | 77.6 ms                                                                                              | 74.8 ms: 1.04x faster                                                                                    |
| xml_etree_process    | 39.7 ms                                                                                              | 38.7 ms: 1.03x faster                                                                                    |
| xml_etree_parse      | 108 ms                                                                                               | 105 ms: 1.02x faster                                                                                     |
| xml_etree_generate   | 56.2 ms                                                                                              | 56.1 ms: 1.00x faster                                                                                    |
| json_dumps           | 6.46 ms                                                                                              | 6.48 ms: 1.00x slower                                                                                    |
| pickle_dict          | 18.1 us                                                                                              | 18.2 us: 1.00x slower                                                                                    |
| pickle_list          | 2.96 us                                                                                              | 2.99 us: 1.01x slower                                                                                    |
| unpickle_list        | 3.07 us                                                                                              | 3.10 us: 1.01x slower                                                                                    |
| unpickle_pure_python | 154 us                                                                                               | 158 us: 1.02x slower                                                                                     |
| Geometric mean       | (ref)                                                                                                | 1.01x faster                                                                                             |

Benchmark hidden because not significant (4): json_loads, pickle_pure_python, pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|------------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 14.8 ms                                                                                              | 11.6 ms: 1.28x faster                                                                                    |
| python_startup         | 16.6 ms                                                                                              | 13.1 ms: 1.27x faster                                                                                    |
| Geometric mean         | (ref)                                                                                                | 1.27x faster                                                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|-----------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| mako      | 7.33 ms                                                                                              | 7.79 ms: 1.06x slower                                                                                    |

All benchmarks:
===============

| Benchmark                | results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json | results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json |
|--------------------------|:----------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|
| python_startup_no_site   | 14.8 ms                                                                                              | 11.6 ms: 1.28x faster                                                                                    |
| python_startup           | 16.6 ms                                                                                              | 13.1 ms: 1.27x faster                                                                                    |
| tornado_http             | 84.4 ms                                                                                              | 69.6 ms: 1.21x faster                                                                                    |
| tomli_loads              | 1.54 sec                                                                                             | 1.40 sec: 1.10x faster                                                                                   |
| richards                 | 33.9 ms                                                                                              | 31.9 ms: 1.06x faster                                                                                    |
| bench_mp_pool            | 48.7 ms                                                                                              | 45.9 ms: 1.06x faster                                                                                    |
| richards_super           | 37.7 ms                                                                                              | 35.7 ms: 1.06x faster                                                                                    |
| pyflate                  | 339 ms                                                                                               | 326 ms: 1.04x faster                                                                                     |
| xml_etree_iterparse      | 77.6 ms                                                                                              | 74.8 ms: 1.04x faster                                                                                    |
| xml_etree_process        | 39.7 ms                                                                                              | 38.7 ms: 1.03x faster                                                                                    |
| coroutines               | 19.2 ms                                                                                              | 18.7 ms: 1.02x faster                                                                                    |
| xml_etree_parse          | 108 ms                                                                                               | 105 ms: 1.02x faster                                                                                     |
| float                    | 56.7 ms                                                                                              | 55.5 ms: 1.02x faster                                                                                    |
| typing_runtime_protocols | 72.2 us                                                                                              | 70.9 us: 1.02x faster                                                                                    |
| generators               | 28.6 ms                                                                                              | 28.3 ms: 1.01x faster                                                                                    |
| async_tree_io            | 707 ms                                                                                               | 699 ms: 1.01x faster                                                                                     |
| async_tree_io_tg         | 672 ms                                                                                               | 666 ms: 1.01x faster                                                                                     |
| json                     | 2.97 ms                                                                                              | 2.95 ms: 1.01x faster                                                                                    |
| chameleon                | 4.84 ms                                                                                              | 4.81 ms: 1.01x faster                                                                                    |
| create_gc_cycles         | 710 us                                                                                               | 705 us: 1.01x faster                                                                                     |
| fannkuch                 | 268 ms                                                                                               | 267 ms: 1.01x faster                                                                                     |
| gc_traversal             | 2.40 ms                                                                                              | 2.39 ms: 1.01x faster                                                                                    |
| async_tree_none_tg       | 260 ms                                                                                               | 259 ms: 1.01x faster                                                                                     |
| sqlglot_parse            | 790 us                                                                                               | 787 us: 1.00x faster                                                                                     |
| xml_etree_generate       | 56.2 ms                                                                                              | 56.1 ms: 1.00x faster                                                                                    |
| sqlite_synth             | 1.60 us                                                                                              | 1.59 us: 1.00x faster                                                                                    |
| asyncio_websockets       | 408 ms                                                                                               | 409 ms: 1.00x slower                                                                                     |
| pprint_safe_repr         | 514 ms                                                                                               | 515 ms: 1.00x slower                                                                                     |
| scimark_sor              | 105 ms                                                                                               | 106 ms: 1.00x slower                                                                                     |
| pprint_pformat           | 1.05 sec                                                                                             | 1.05 sec: 1.00x slower                                                                                   |
| logging_simple           | 3.44 us                                                                                              | 3.45 us: 1.00x slower                                                                                    |
| json_dumps               | 6.46 ms                                                                                              | 6.48 ms: 1.00x slower                                                                                    |
| pickle_dict              | 18.1 us                                                                                              | 18.2 us: 1.00x slower                                                                                    |
| sqlglot_normalize        | 181 ms                                                                                               | 182 ms: 1.00x slower                                                                                     |
| sqlglot_transpile        | 968 us                                                                                               | 973 us: 1.00x slower                                                                                     |
| deltablue                | 2.44 ms                                                                                              | 2.45 ms: 1.01x slower                                                                                    |
| pickle_list              | 2.96 us                                                                                              | 2.99 us: 1.01x slower                                                                                    |
| deepcopy_reduce          | 1.97 us                                                                                              | 1.98 us: 1.01x slower                                                                                    |
| scimark_lu               | 74.2 ms                                                                                              | 74.8 ms: 1.01x slower                                                                                    |
| telco                    | 4.47 ms                                                                                              | 4.51 ms: 1.01x slower                                                                                    |
| deepcopy                 | 224 us                                                                                               | 226 us: 1.01x slower                                                                                     |
| logging_format           | 3.72 us                                                                                              | 3.76 us: 1.01x slower                                                                                    |
| unpickle_list            | 3.07 us                                                                                              | 3.10 us: 1.01x slower                                                                                    |
| logging_silent           | 69.5 ns                                                                                              | 70.3 ns: 1.01x slower                                                                                    |
| sympy_expand             | 238 ms                                                                                               | 241 ms: 1.01x slower                                                                                     |
| docutils                 | 1.46 sec                                                                                             | 1.48 sec: 1.01x slower                                                                                   |
| dulwich_log              | 29.4 ms                                                                                              | 29.8 ms: 1.01x slower                                                                                    |
| unpack_sequence          | 28.0 ns                                                                                              | 28.4 ns: 1.02x slower                                                                                    |
| regex_v8                 | 17.1 ms                                                                                              | 17.4 ms: 1.02x slower                                                                                    |
| crypto_pyaes             | 48.2 ms                                                                                              | 49.1 ms: 1.02x slower                                                                                    |
| meteor_contest           | 72.9 ms                                                                                              | 74.3 ms: 1.02x slower                                                                                    |
| regex_effbot             | 2.49 ms                                                                                              | 2.54 ms: 1.02x slower                                                                                    |
| sympy_str                | 138 ms                                                                                               | 141 ms: 1.02x slower                                                                                     |
| sqlglot_optimize         | 33.7 ms                                                                                              | 34.4 ms: 1.02x slower                                                                                    |
| async_generators         | 297 ms                                                                                               | 303 ms: 1.02x slower                                                                                     |
| unpickle_pure_python     | 154 us                                                                                               | 158 us: 1.02x slower                                                                                     |
| deepcopy_memo            | 25.7 us                                                                                              | 26.3 us: 1.02x slower                                                                                    |
| regex_compile            | 73.4 ms                                                                                              | 75.1 ms: 1.02x slower                                                                                    |
| nqueens                  | 60.1 ms                                                                                              | 61.6 ms: 1.02x slower                                                                                    |
| nbody                    | 74.0 ms                                                                                              | 75.9 ms: 1.03x slower                                                                                    |
| regex_dna                | 146 ms                                                                                               | 150 ms: 1.03x slower                                                                                     |
| raytrace                 | 171 ms                                                                                               | 176 ms: 1.03x slower                                                                                     |
| scimark_monte_carlo      | 47.0 ms                                                                                              | 48.5 ms: 1.03x slower                                                                                    |
| sympy_integrate          | 10.7 ms                                                                                              | 11.1 ms: 1.04x slower                                                                                    |
| mdp                      | 1.56 sec                                                                                             | 1.61 sec: 1.04x slower                                                                                   |
| bench_thread_pool        | 484 us                                                                                               | 504 us: 1.04x slower                                                                                     |
| sympy_sum                | 72.4 ms                                                                                              | 75.3 ms: 1.04x slower                                                                                    |
| chaos                    | 39.4 ms                                                                                              | 41.0 ms: 1.04x slower                                                                                    |
| comprehensions           | 12.1 us                                                                                              | 12.6 us: 1.04x slower                                                                                    |
| scimark_fft              | 203 ms                                                                                               | 213 ms: 1.05x slower                                                                                     |
| go                       | 105 ms                                                                                               | 110 ms: 1.05x slower                                                                                     |
| spectral_norm            | 74.4 ms                                                                                              | 78.8 ms: 1.06x slower                                                                                    |
| scimark_sparse_mat_mult  | 3.12 ms                                                                                              | 3.31 ms: 1.06x slower                                                                                    |
| mako                     | 7.33 ms                                                                                              | 7.79 ms: 1.06x slower                                                                                    |
| hexiom                   | 4.56 ms                                                                                              | 4.91 ms: 1.08x slower                                                                                    |
| 2to3                     | 174 ms                                                                                               | 190 ms: 1.09x slower                                                                                     |
| mypy2                    | 385 ms                                                                                               | 577 ms: 1.50x slower                                                                                     |
| Geometric mean           | (ref)                                                                                                | 1.00x slower                                                                                             |

Benchmark hidden because not significant (15): asyncio_tcp_ssl, asyncio_tcp, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg, coverage, async_tree_none, async_tree_cpu_io_mixed_tg, pathlib, json_loads, pickle_pure_python, pickle, pycparser, pidigits, unpickle
Ignored benchmarks (18) of results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json: aiohttp, async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift
Ignored benchmarks (1) of results/bm-20240215-3.13.0a4-9d34f60-JIT/bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60.json: dask

- Geometric mean (including insignificant results): 1.004x slower
# HPT report

- Reliability score: 89.38% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.96x