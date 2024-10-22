# Results vs. base

- fork: brandtbucher
- ref: justin_likely
- machine: linux-x86_64
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.01x slower
- HPT reliability: 99.82%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 277 ms                                                                 | 278 ms: 1.00x slower                                                  |
| docutils       | 2.91 sec                                                               | 2.92 sec: 1.00x slower                                                |
| html5lib       | 64.7 ms                                                                | 64.0 ms: 1.01x faster                                                 |
| tornado_http   | 94.5 ms                                                                | 95.0 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines       | 23.0 ms                                                                | 22.9 ms: 1.01x faster                                                 |
| async_tree_io_tg | 975 ms                                                                 | 971 ms: 1.00x faster                                                  |
| asyncio_tcp_ssl  | 1.81 sec                                                               | 1.80 sec: 1.00x faster                                                |
| Geometric mean   | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (10): async_tree_io, async_tree_none, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, asyncio_tcp, asyncio_websockets, async_tree_none_tg, async_generators, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 186 ms: 1.00x faster                                                  |
| float          | 75.6 ms                                                                | 76.0 ms: 1.01x slower                                                 |
| nbody          | 80.1 ms                                                                | 84.5 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.81 ms                                                                | 3.68 ms: 1.04x faster                                                 |
| regex_v8       | 25.5 ms                                                                | 24.7 ms: 1.03x faster                                                 |
| regex_dna      | 217 ms                                                                 | 216 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle             | 14.9 us                                                                | 14.3 us: 1.04x faster                                                 |
| json_loads           | 26.6 us                                                                | 26.5 us: 1.00x faster                                                 |
| unpickle_pure_python | 216 us                                                                 | 218 us: 1.01x slower                                                  |
| tomli_loads          | 1.91 sec                                                               | 1.93 sec: 1.01x slower                                                |
| unpickle_list        | 5.45 us                                                                | 5.53 us: 1.01x slower                                                 |
| pickle_list          | 5.02 us                                                                | 5.13 us: 1.02x slower                                                 |
| xml_etree_parse      | 145 ms                                                                 | 149 ms: 1.03x slower                                                  |
| json_dumps           | 10.9 ms                                                                | 11.2 ms: 1.03x slower                                                 |
| pickle               | 11.5 us                                                                | 11.9 us: 1.03x slower                                                 |
| pickle_dict          | 33.6 us                                                                | 34.8 us: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_iterparse, xml_etree_process, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                                | 11.9 ms: 1.00x slower                                                 |
| python_startup_no_site | 7.08 ms                                                                | 7.09 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 25.4 ms                                                                | 25.2 ms: 1.01x faster                                                 |
| mako            | 9.97 ms                                                                | 10.1 ms: 1.02x slower                                                 |
| django_template | 35.9 ms                                                                | 36.7 ms: 1.02x slower                                                 |
| genshi_xml      | 58.6 ms                                                                | 61.9 ms: 1.06x slower                                                 |
| Geometric mean  | (ref)                                                                  | 1.02x slower                                                          |

All benchmarks:
===============

| Benchmark               | bm-20241017-linux-x86_64-python-d8c864816121547338ef-3.14.0a1+-d8c8648 | bm-20241018-linux-x86_64-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle                | 14.9 us                                                                | 14.3 us: 1.04x faster                                                 |
| regex_effbot            | 3.81 ms                                                                | 3.68 ms: 1.04x faster                                                 |
| regex_v8                | 25.5 ms                                                                | 24.7 ms: 1.03x faster                                                 |
| pycparser               | 1.20 sec                                                               | 1.17 sec: 1.03x faster                                                |
| logging_format          | 6.26 us                                                                | 6.11 us: 1.02x faster                                                 |
| scimark_sor             | 120 ms                                                                 | 118 ms: 1.02x faster                                                  |
| logging_simple          | 5.74 us                                                                | 5.62 us: 1.02x faster                                                 |
| json                    | 4.96 ms                                                                | 4.88 ms: 1.01x faster                                                 |
| richards_super          | 47.8 ms                                                                | 47.2 ms: 1.01x faster                                                 |
| gc_traversal            | 4.57 ms                                                                | 4.52 ms: 1.01x faster                                                 |
| html5lib                | 64.7 ms                                                                | 64.0 ms: 1.01x faster                                                 |
| generators              | 35.5 ms                                                                | 35.2 ms: 1.01x faster                                                 |
| scimark_lu              | 114 ms                                                                 | 113 ms: 1.01x faster                                                  |
| spectral_norm           | 114 ms                                                                 | 113 ms: 1.01x faster                                                  |
| genshi_text             | 25.4 ms                                                                | 25.2 ms: 1.01x faster                                                 |
| coroutines              | 23.0 ms                                                                | 22.9 ms: 1.01x faster                                                 |
| async_tree_io_tg        | 975 ms                                                                 | 971 ms: 1.00x faster                                                  |
| json_loads              | 26.6 us                                                                | 26.5 us: 1.00x faster                                                 |
| create_gc_cycles        | 2.69 ms                                                                | 2.68 ms: 1.00x faster                                                 |
| scimark_monte_carlo     | 64.2 ms                                                                | 63.9 ms: 1.00x faster                                                 |
| asyncio_tcp_ssl         | 1.81 sec                                                               | 1.80 sec: 1.00x faster                                                |
| regex_dna               | 217 ms                                                                 | 216 ms: 1.00x faster                                                  |
| pidigits                | 186 ms                                                                 | 186 ms: 1.00x faster                                                  |
| python_startup          | 11.9 ms                                                                | 11.9 ms: 1.00x slower                                                 |
| python_startup_no_site  | 7.08 ms                                                                | 7.09 ms: 1.00x slower                                                 |
| 2to3                    | 277 ms                                                                 | 278 ms: 1.00x slower                                                  |
| docutils                | 2.91 sec                                                               | 2.92 sec: 1.00x slower                                                |
| bench_thread_pool       | 875 us                                                                 | 878 us: 1.00x slower                                                  |
| sympy_integrate         | 23.5 ms                                                                | 23.6 ms: 1.00x slower                                                 |
| tornado_http            | 94.5 ms                                                                | 95.0 ms: 1.00x slower                                                 |
| bpe_tokeniser           | 4.41 sec                                                               | 4.44 sec: 1.01x slower                                                |
| float                   | 75.6 ms                                                                | 76.0 ms: 1.01x slower                                                 |
| dulwich_log             | 66.2 ms                                                                | 66.7 ms: 1.01x slower                                                 |
| raytrace                | 276 ms                                                                 | 278 ms: 1.01x slower                                                  |
| sqlglot_transpile       | 1.68 ms                                                                | 1.69 ms: 1.01x slower                                                 |
| hexiom                  | 7.01 ms                                                                | 7.07 ms: 1.01x slower                                                 |
| go                      | 133 ms                                                                 | 134 ms: 1.01x slower                                                  |
| sympy_expand            | 500 ms                                                                 | 505 ms: 1.01x slower                                                  |
| sqlglot_normalize       | 114 ms                                                                 | 115 ms: 1.01x slower                                                  |
| unpickle_pure_python    | 216 us                                                                 | 218 us: 1.01x slower                                                  |
| tomli_loads             | 1.91 sec                                                               | 1.93 sec: 1.01x slower                                                |
| sqlglot_parse           | 1.32 ms                                                                | 1.34 ms: 1.01x slower                                                 |
| deepcopy                | 270 us                                                                 | 274 us: 1.01x slower                                                  |
| pyflate                 | 448 ms                                                                 | 455 ms: 1.01x slower                                                  |
| deepcopy_reduce         | 2.77 us                                                                | 2.81 us: 1.01x slower                                                 |
| pathlib                 | 15.9 ms                                                                | 16.2 ms: 1.01x slower                                                 |
| unpickle_list           | 5.45 us                                                                | 5.53 us: 1.01x slower                                                 |
| deepcopy_memo           | 29.4 us                                                                | 29.8 us: 1.01x slower                                                 |
| mako                    | 9.97 ms                                                                | 10.1 ms: 1.02x slower                                                 |
| sqlglot_optimize        | 59.5 ms                                                                | 60.6 ms: 1.02x slower                                                 |
| comprehensions          | 17.1 us                                                                | 17.4 us: 1.02x slower                                                 |
| scimark_fft             | 317 ms                                                                 | 323 ms: 1.02x slower                                                  |
| django_template         | 35.9 ms                                                                | 36.7 ms: 1.02x slower                                                 |
| pickle_list             | 5.02 us                                                                | 5.13 us: 1.02x slower                                                 |
| xml_etree_parse         | 145 ms                                                                 | 149 ms: 1.03x slower                                                  |
| json_dumps              | 10.9 ms                                                                | 11.2 ms: 1.03x slower                                                 |
| pickle                  | 11.5 us                                                                | 11.9 us: 1.03x slower                                                 |
| unpack_sequence         | 105 ns                                                                 | 108 ns: 1.03x slower                                                  |
| pickle_dict             | 33.6 us                                                                | 34.8 us: 1.04x slower                                                 |
| pprint_safe_repr        | 710 ms                                                                 | 742 ms: 1.05x slower                                                  |
| fannkuch                | 383 ms                                                                 | 401 ms: 1.05x slower                                                  |
| nbody                   | 80.1 ms                                                                | 84.5 ms: 1.05x slower                                                 |
| genshi_xml              | 58.6 ms                                                                | 61.9 ms: 1.06x slower                                                 |
| scimark_sparse_mat_mult | 4.61 ms                                                                | 4.90 ms: 1.06x slower                                                 |
| pprint_pformat          | 1.46 sec                                                               | 1.56 sec: 1.07x slower                                                |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (33): async_tree_io, meteor_contest, deltablue, async_tree_none, xml_etree_generate, async_tree_cpu_io_mixed, bench_mp_pool, logging_silent, async_tree_cpu_io_mixed_tg, mdp, chaos, thrift, nqueens, asyncio_tcp, sympy_sum, xml_etree_iterparse, asyncio_websockets, async_tree_none_tg, xml_etree_process, async_generators, pylint, sympy_str, typing_runtime_protocols, async_tree_memoization_tg, regex_compile, sphinx, richards, coverage, telco, sqlite_synth, pickle_pure_python, crypto_pyaes, async_tree_memoization

# HPT report

- Reliability score: 99.82% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x