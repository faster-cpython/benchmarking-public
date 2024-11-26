# Results vs. base

- fork: brandtbucher
- ref: justin_no_externs
- machine: darwin-arm64
- commit hash: 9698931
- commit date: 2024-10-24
- overall geometric mean: 1.024x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 183 ms                                                                 | 191 ms: 1.04x slower                                                      |
| docutils       | 1.56 sec                                                               | 1.58 sec: 1.01x slower                                                    |
| html5lib       | 32.8 ms                                                                | 33.0 ms: 1.01x slower                                                     |
| sphinx         | 663 ms                                                                 | 670 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|--------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg | 218 ms                                                                 | 214 ms: 1.02x faster                                                      |
| coroutines         | 16.4 ms                                                                | 16.3 ms: 1.01x faster                                                     |
| asyncio_websockets | 243 ms                                                                 | 242 ms: 1.00x faster                                                      |
| async_tree_io_tg   | 611 ms                                                                 | 614 ms: 1.01x slower                                                      |
| async_tree_none    | 198 ms                                                                 | 200 ms: 1.01x slower                                                      |
| async_generators   | 292 ms                                                                 | 298 ms: 1.02x slower                                                      |
| async_tree_eager   | 63.5 ms                                                                | 65.9 ms: 1.04x slower                                                     |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (12): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_tg, async_tree_eager_memoization_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_memoization_tg, async_tree_eager_cpu_io_mixed, async_tree_memoization, async_tree_io, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 283 ms                                                                 | 283 ms: 1.00x slower                                                      |
| nbody          | 65.9 ms                                                                | 66.1 ms: 1.00x slower                                                     |
| float          | 48.3 ms                                                                | 49.8 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 142 ms                                                                 | 142 ms: 1.00x faster                                                      |
| regex_v8       | 16.7 ms                                                                | 16.7 ms: 1.00x slower                                                     |
| regex_compile  | 74.9 ms                                                                | 79.4 ms: 1.06x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 7.15 ms                                                                | 7.23 ms: 1.01x slower                                                     |
| xml_etree_iterparse  | 73.0 ms                                                                | 73.9 ms: 1.01x slower                                                     |
| pickle_pure_python   | 178 us                                                                 | 181 us: 1.02x slower                                                      |
| unpickle_pure_python | 133 us                                                                 | 137 us: 1.02x slower                                                      |
| xml_etree_process    | 34.6 ms                                                                | 35.7 ms: 1.03x slower                                                     |
| xml_etree_generate   | 49.4 ms                                                                | 51.2 ms: 1.04x slower                                                     |
| tomli_loads          | 1.25 sec                                                               | 1.33 sec: 1.07x slower                                                    |
| Geometric mean       | (ref)                                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 18.5 ms                                                                | 18.0 ms: 1.03x faster                                                     |
| python_startup_no_site | 14.4 ms                                                                | 14.0 ms: 1.03x faster                                                     |
| Geometric mean         | (ref)                                                                  | 1.03x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 17.1 ms                                                                | 16.8 ms: 1.01x faster                                                     |
| genshi_xml      | 42.6 ms                                                                | 45.7 ms: 1.07x slower                                                     |
| django_template | 23.0 ms                                                                | 25.0 ms: 1.09x slower                                                     |
| mako            | 6.44 ms                                                                | 7.03 ms: 1.09x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.06x slower                                                              |

All benchmarks:
===============

| Benchmark                | bm-20241022-darwin-arm64-python-34653bba644aa5481613-3.14.0a1+-34653bb | bm-20241024-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|--------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup           | 18.5 ms                                                                | 18.0 ms: 1.03x faster                                                     |
| python_startup_no_site   | 14.4 ms                                                                | 14.0 ms: 1.03x faster                                                     |
| async_tree_none_tg       | 218 ms                                                                 | 214 ms: 1.02x faster                                                      |
| json                     | 2.91 ms                                                                | 2.87 ms: 1.01x faster                                                     |
| genshi_text              | 17.1 ms                                                                | 16.8 ms: 1.01x faster                                                     |
| thrift                   | 426 us                                                                 | 422 us: 1.01x faster                                                      |
| coroutines               | 16.4 ms                                                                | 16.3 ms: 1.01x faster                                                     |
| bench_mp_pool            | 62.0 ms                                                                | 61.6 ms: 1.01x faster                                                     |
| coverage                 | 43.7 ms                                                                | 43.5 ms: 1.01x faster                                                     |
| asyncio_websockets       | 243 ms                                                                 | 242 ms: 1.00x faster                                                      |
| regex_dna                | 142 ms                                                                 | 142 ms: 1.00x faster                                                      |
| pidigits                 | 283 ms                                                                 | 283 ms: 1.00x slower                                                      |
| deepcopy_reduce          | 1.53 us                                                                | 1.54 us: 1.00x slower                                                     |
| create_gc_cycles         | 1.33 ms                                                                | 1.33 ms: 1.00x slower                                                     |
| nbody                    | 65.9 ms                                                                | 66.1 ms: 1.00x slower                                                     |
| regex_v8                 | 16.7 ms                                                                | 16.7 ms: 1.00x slower                                                     |
| logging_simple           | 3.17 us                                                                | 3.18 us: 1.00x slower                                                     |
| mdp                      | 1.55 sec                                                               | 1.55 sec: 1.01x slower                                                    |
| async_tree_io_tg         | 611 ms                                                                 | 614 ms: 1.01x slower                                                      |
| html5lib                 | 32.8 ms                                                                | 33.0 ms: 1.01x slower                                                     |
| async_tree_none          | 198 ms                                                                 | 200 ms: 1.01x slower                                                      |
| sqlalchemy_declarative   | 61.8 ms                                                                | 62.4 ms: 1.01x slower                                                     |
| docutils                 | 1.56 sec                                                               | 1.58 sec: 1.01x slower                                                    |
| logging_format           | 3.44 us                                                                | 3.48 us: 1.01x slower                                                     |
| json_dumps               | 7.15 ms                                                                | 7.23 ms: 1.01x slower                                                     |
| sphinx                   | 663 ms                                                                 | 670 ms: 1.01x slower                                                      |
| xml_etree_iterparse      | 73.0 ms                                                                | 73.9 ms: 1.01x slower                                                     |
| typing_runtime_protocols | 98.1 us                                                                | 99.5 us: 1.01x slower                                                     |
| pickle_pure_python       | 178 us                                                                 | 181 us: 1.02x slower                                                      |
| bench_thread_pool        | 473 us                                                                 | 481 us: 1.02x slower                                                      |
| async_generators         | 292 ms                                                                 | 298 ms: 1.02x slower                                                      |
| crypto_pyaes             | 54.5 ms                                                                | 55.6 ms: 1.02x slower                                                     |
| unpickle_pure_python     | 133 us                                                                 | 137 us: 1.02x slower                                                      |
| scimark_lu               | 64.5 ms                                                                | 66.1 ms: 1.03x slower                                                     |
| sqlalchemy_imperative    | 6.55 ms                                                                | 6.73 ms: 1.03x slower                                                     |
| generators               | 25.3 ms                                                                | 26.0 ms: 1.03x slower                                                     |
| xml_etree_process        | 34.6 ms                                                                | 35.7 ms: 1.03x slower                                                     |
| float                    | 48.3 ms                                                                | 49.8 ms: 1.03x slower                                                     |
| pycparser                | 683 ms                                                                 | 705 ms: 1.03x slower                                                      |
| meteor_contest           | 74.4 ms                                                                | 76.8 ms: 1.03x slower                                                     |
| bpe_tokeniser            | 3.04 sec                                                               | 3.14 sec: 1.03x slower                                                    |
| sympy_sum                | 79.8 ms                                                                | 82.6 ms: 1.03x slower                                                     |
| fannkuch                 | 265 ms                                                                 | 275 ms: 1.04x slower                                                      |
| xml_etree_generate       | 49.4 ms                                                                | 51.2 ms: 1.04x slower                                                     |
| dulwich_log              | 28.8 ms                                                                | 29.8 ms: 1.04x slower                                                     |
| sympy_expand             | 247 ms                                                                 | 256 ms: 1.04x slower                                                      |
| async_tree_eager         | 63.5 ms                                                                | 65.9 ms: 1.04x slower                                                     |
| deltablue                | 2.41 ms                                                                | 2.51 ms: 1.04x slower                                                     |
| sympy_str                | 152 ms                                                                 | 158 ms: 1.04x slower                                                      |
| 2to3                     | 183 ms                                                                 | 191 ms: 1.04x slower                                                      |
| sqlglot_normalize        | 187 ms                                                                 | 195 ms: 1.04x slower                                                      |
| sqlglot_parse            | 879 us                                                                 | 916 us: 1.04x slower                                                      |
| sqlglot_transpile        | 1.08 ms                                                                | 1.12 ms: 1.04x slower                                                     |
| deepcopy                 | 156 us                                                                 | 163 us: 1.04x slower                                                      |
| raytrace                 | 170 ms                                                                 | 178 ms: 1.04x slower                                                      |
| sqlglot_optimize         | 37.4 ms                                                                | 39.1 ms: 1.05x slower                                                     |
| chaos                    | 41.6 ms                                                                | 43.7 ms: 1.05x slower                                                     |
| nqueens                  | 58.6 ms                                                                | 61.6 ms: 1.05x slower                                                     |
| pyflate                  | 326 ms                                                                 | 343 ms: 1.05x slower                                                      |
| richards                 | 34.1 ms                                                                | 36.0 ms: 1.05x slower                                                     |
| spectral_norm            | 69.7 ms                                                                | 73.6 ms: 1.06x slower                                                     |
| scimark_monte_carlo      | 45.3 ms                                                                | 47.9 ms: 1.06x slower                                                     |
| richards_super           | 37.9 ms                                                                | 40.1 ms: 1.06x slower                                                     |
| sympy_integrate          | 12.5 ms                                                                | 13.2 ms: 1.06x slower                                                     |
| regex_compile            | 74.9 ms                                                                | 79.4 ms: 1.06x slower                                                     |
| go                       | 100 ms                                                                 | 106 ms: 1.06x slower                                                      |
| scimark_fft              | 190 ms                                                                 | 203 ms: 1.07x slower                                                      |
| pprint_safe_repr         | 500 ms                                                                 | 533 ms: 1.07x slower                                                      |
| scimark_sor              | 85.9 ms                                                                | 91.6 ms: 1.07x slower                                                     |
| tomli_loads              | 1.25 sec                                                               | 1.33 sec: 1.07x slower                                                    |
| logging_silent           | 70.0 ns                                                                | 74.8 ns: 1.07x slower                                                     |
| genshi_xml               | 42.6 ms                                                                | 45.7 ms: 1.07x slower                                                     |
| scimark_sparse_mat_mult  | 3.16 ms                                                                | 3.42 ms: 1.08x slower                                                     |
| django_template          | 23.0 ms                                                                | 25.0 ms: 1.09x slower                                                     |
| mako                     | 6.44 ms                                                                | 7.03 ms: 1.09x slower                                                     |
| deepcopy_memo            | 16.5 us                                                                | 18.1 us: 1.09x slower                                                     |
| hexiom                   | 5.01 ms                                                                | 5.52 ms: 1.10x slower                                                     |
| pprint_pformat           | 991 ms                                                                 | 1.13 sec: 1.14x slower                                                    |
| Geometric mean           | (ref)                                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (21): comprehensions, async_tree_cpu_io_mixed_tg, xml_etree_parse, telco, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_tg, regex_effbot, json_loads, gc_traversal, async_tree_eager_memoization_tg, async_tree_eager_io, pathlib, async_tree_eager_io_tg, async_tree_memoization_tg, async_tree_eager_cpu_io_mixed, async_tree_memoization, async_tree_io, async_tree_eager_memoization, tornado_http, pylint

- Geometric mean (including insignificant results): 1.024x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.00x