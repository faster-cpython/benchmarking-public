# Results vs. base

- fork: brandtbucher
- ref: trace_through
- machine: linux-x86_64
- commit hash: b1a2c42
- commit date: 2024-09-06
- overall geometric mean: 1.00x slower
- HPT reliability: 81.50%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 275 ms                                                                | 278 ms: 1.01x slower                                                 |
| docutils       | 3.03 sec                                                              | 3.00 sec: 1.01x faster                                               |
| html5lib       | 64.7 ms                                                               | 62.4 ms: 1.04x faster                                                |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_none_tg      | 313 ms                                                                | 307 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed | 571 ms                                                                | 562 ms: 1.02x faster                                                 |
| async_tree_io           | 932 ms                                                                | 926 ms: 1.01x faster                                                 |
| asyncio_tcp_ssl         | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                               |
| coroutines              | 22.8 ms                                                               | 23.0 ms: 1.01x slower                                                |
| Geometric mean          | (ref)                                                                 | 1.01x faster                                                         |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, asyncio_websockets, async_tree_none, asyncio_tcp, async_generators, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 79.1 ms                                                               | 81.0 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                         |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna      | 219 ms                                                                | 212 ms: 1.03x faster                                                 |
| regex_effbot   | 3.55 ms                                                               | 3.47 ms: 1.02x faster                                                |
| regex_v8       | 24.8 ms                                                               | 24.4 ms: 1.01x faster                                                |
| regex_compile  | 142 ms                                                                | 145 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_process    | 55.2 ms                                                               | 54.0 ms: 1.02x faster                                                |
| xml_etree_generate   | 77.8 ms                                                               | 76.5 ms: 1.02x faster                                                |
| unpickle_pure_python | 216 us                                                                | 213 us: 1.02x faster                                                 |
| json_loads           | 28.6 us                                                               | 28.7 us: 1.00x slower                                                |
| xml_etree_iterparse  | 98.0 ms                                                               | 98.5 ms: 1.01x slower                                                |
| tomli_loads          | 1.93 sec                                                              | 1.95 sec: 1.01x slower                                               |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (3): xml_etree_parse, json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                               | 7.17 ms: 1.01x slower                                                |
| python_startup         | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                               | 55.9 ms: 1.04x faster                                                |
| mako            | 9.77 ms                                                               | 9.85 ms: 1.01x slower                                                |
| genshi_text     | 24.2 ms                                                               | 24.5 ms: 1.01x slower                                                |
| django_template | 35.6 ms                                                               | 36.6 ms: 1.03x slower                                                |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                         |

All benchmarks:
===============

| Benchmark                | bm-20240903-linux-x86_64-python-cfbc841ef3c27b3e65d1-3.14.0a0-cfbc841 | bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| json                     | 5.56 ms                                                               | 5.30 ms: 1.05x faster                                                |
| logging_silent           | 104 ns                                                                | 100.0 ns: 1.04x faster                                               |
| genshi_xml               | 58.1 ms                                                               | 55.9 ms: 1.04x faster                                                |
| deepcopy_memo            | 27.3 us                                                               | 26.4 us: 1.04x faster                                                |
| html5lib                 | 64.7 ms                                                               | 62.4 ms: 1.04x faster                                                |
| regex_dna                | 219 ms                                                                | 212 ms: 1.03x faster                                                 |
| richards_super           | 45.4 ms                                                               | 44.0 ms: 1.03x faster                                                |
| deltablue                | 3.19 ms                                                               | 3.11 ms: 1.03x faster                                                |
| deepcopy_reduce          | 2.68 us                                                               | 2.62 us: 1.02x faster                                                |
| xml_etree_process        | 55.2 ms                                                               | 54.0 ms: 1.02x faster                                                |
| pprint_pformat           | 1.52 sec                                                              | 1.48 sec: 1.02x faster                                               |
| regex_effbot             | 3.55 ms                                                               | 3.47 ms: 1.02x faster                                                |
| sqlglot_transpile        | 1.70 ms                                                               | 1.67 ms: 1.02x faster                                                |
| xml_etree_generate       | 77.8 ms                                                               | 76.5 ms: 1.02x faster                                                |
| async_tree_none_tg       | 313 ms                                                                | 307 ms: 1.02x faster                                                 |
| unpickle_pure_python     | 216 us                                                                | 213 us: 1.02x faster                                                 |
| async_tree_cpu_io_mixed  | 571 ms                                                                | 562 ms: 1.02x faster                                                 |
| regex_v8                 | 24.8 ms                                                               | 24.4 ms: 1.01x faster                                                |
| sqlglot_parse            | 1.34 ms                                                               | 1.33 ms: 1.01x faster                                                |
| docutils                 | 3.03 sec                                                              | 3.00 sec: 1.01x faster                                               |
| pyflate                  | 452 ms                                                                | 449 ms: 1.01x faster                                                 |
| async_tree_io            | 932 ms                                                                | 926 ms: 1.01x faster                                                 |
| bench_thread_pool        | 836 us                                                                | 834 us: 1.00x faster                                                 |
| asyncio_tcp_ssl          | 1.80 sec                                                              | 1.80 sec: 1.00x slower                                               |
| json_loads               | 28.6 us                                                               | 28.7 us: 1.00x slower                                                |
| create_gc_cycles         | 1.75 ms                                                               | 1.76 ms: 1.00x slower                                                |
| xml_etree_iterparse      | 98.0 ms                                                               | 98.5 ms: 1.01x slower                                                |
| sympy_expand             | 504 ms                                                                | 507 ms: 1.01x slower                                                 |
| gc_traversal             | 3.56 ms                                                               | 3.59 ms: 1.01x slower                                                |
| mako                     | 9.77 ms                                                               | 9.85 ms: 1.01x slower                                                |
| 2to3                     | 275 ms                                                                | 278 ms: 1.01x slower                                                 |
| python_startup_no_site   | 7.11 ms                                                               | 7.17 ms: 1.01x slower                                                |
| tomli_loads              | 1.93 sec                                                              | 1.95 sec: 1.01x slower                                               |
| crypto_pyaes             | 65.9 ms                                                               | 66.7 ms: 1.01x slower                                                |
| coroutines               | 22.8 ms                                                               | 23.0 ms: 1.01x slower                                                |
| sqlglot_optimize         | 57.7 ms                                                               | 58.4 ms: 1.01x slower                                                |
| spectral_norm            | 99.2 ms                                                               | 100 ms: 1.01x slower                                                 |
| sympy_integrate          | 22.7 ms                                                               | 23.0 ms: 1.01x slower                                                |
| python_startup           | 10.5 ms                                                               | 10.6 ms: 1.01x slower                                                |
| genshi_text              | 24.2 ms                                                               | 24.5 ms: 1.01x slower                                                |
| sympy_sum                | 173 ms                                                                | 175 ms: 1.01x slower                                                 |
| richards                 | 39.2 ms                                                               | 39.8 ms: 1.01x slower                                                |
| sympy_str                | 299 ms                                                                | 304 ms: 1.02x slower                                                 |
| bpe_tokeniser            | 4.43 sec                                                              | 4.50 sec: 1.02x slower                                               |
| regex_compile            | 142 ms                                                                | 145 ms: 1.02x slower                                                 |
| telco                    | 7.82 ms                                                               | 7.99 ms: 1.02x slower                                                |
| nbody                    | 79.1 ms                                                               | 81.0 ms: 1.02x slower                                                |
| typing_runtime_protocols | 163 us                                                                | 167 us: 1.02x slower                                                 |
| django_template          | 35.6 ms                                                               | 36.6 ms: 1.03x slower                                                |
| dulwich_log              | 68.8 ms                                                               | 70.7 ms: 1.03x slower                                                |
| meteor_contest           | 106 ms                                                                | 109 ms: 1.03x slower                                                 |
| go                       | 130 ms                                                                | 134 ms: 1.03x slower                                                 |
| scimark_lu               | 109 ms                                                                | 113 ms: 1.03x slower                                                 |
| scimark_fft              | 303 ms                                                                | 316 ms: 1.04x slower                                                 |
| scimark_sparse_mat_mult  | 4.20 ms                                                               | 4.43 ms: 1.06x slower                                                |
| mdp                      | 2.54 sec                                                              | 2.72 sec: 1.07x slower                                               |
| hexiom                   | 6.85 ms                                                               | 7.73 ms: 1.13x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (33): async_tree_cpu_io_mixed_tg, async_tree_io_tg, pprint_safe_repr, async_tree_memoization_tg, coverage, deepcopy, logging_simple, pathlib, asyncio_websockets, scimark_monte_carlo, chaos, async_tree_none, xml_etree_parse, asyncio_tcp, thrift, bench_mp_pool, pidigits, float, raytrace, logging_format, async_generators, sqlglot_normalize, tornado_http, scimark_sor, async_tree_memoization, comprehensions, json_dumps, generators, pickle_pure_python, fannkuch, pylint, nqueens, pycparser
Ignored benchmarks (7) of results/bm-20240906-3.14.0a0-b1a2c42-JIT/bm-20240906-linux-x86_64-brandtbucher-trace_through-3.14.0a0-b1a2c42.json: pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 81.50% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x