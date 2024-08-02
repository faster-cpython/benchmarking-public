# Results vs. base

- fork: brandtbucher
- ref: no_cold_exits
- machine: darwin-arm64
- commit hash: a1bdb94
- commit date: 2024-06-18
- overall geometric mean: 1.00x faster
- HPT reliability: 63.45%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.90x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 171 ms                                                                | 170 ms: 1.01x faster                                                 |
| html5lib       | 30.8 ms                                                               | 30.7 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark           | bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|---------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_eager    | 63.2 ms                                                               | 63.4 ms: 1.00x slower                                                |
| async_tree_eager_tg | 42.0 ms                                                               | 42.3 ms: 1.01x slower                                                |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (14): async_tree_eager_cpu_io_mixed, async_tree_eager_io_tg, async_tree_io_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization_tg, async_tree_none, async_tree_eager_io, async_tree_none_tg, async_tree_eager_memoization, async_tree_memoization, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 46.6 ms                                                               | 46.4 ms: 1.00x faster                                                |
| nbody          | 63.5 ms                                                               | 63.6 ms: 1.00x slower                                                |
| pidigits       | 282 ms                                                                | 286 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna      | 149 ms                                                                | 149 ms: 1.00x slower                                                 |
| regex_effbot   | 2.56 ms                                                               | 2.56 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle               | 7.54 us                                                               | 7.49 us: 1.01x faster                                                |
| json_dumps           | 6.29 ms                                                               | 6.26 ms: 1.00x faster                                                |
| xml_etree_process    | 35.9 ms                                                               | 36.1 ms: 1.01x slower                                                |
| unpickle_pure_python | 131 us                                                                | 132 us: 1.01x slower                                                 |
| unpickle_list        | 2.91 us                                                               | 2.93 us: 1.01x slower                                                |
| pickle_list          | 2.98 us                                                               | 3.02 us: 1.01x slower                                                |
| pickle_dict          | 18.3 us                                                               | 18.6 us: 1.02x slower                                                |
| pickle_pure_python   | 173 us                                                                | 176 us: 1.02x slower                                                 |
| tomli_loads          | 1.25 sec                                                              | 1.27 sec: 1.02x slower                                               |
| xml_etree_generate   | 51.2 ms                                                               | 52.2 ms: 1.02x slower                                                |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                         |

Benchmark hidden because not significant (4): unpickle, xml_etree_parse, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 13.5 ms                                                               | 12.3 ms: 1.09x faster                                                |
| python_startup         | 16.0 ms                                                               | 14.9 ms: 1.07x faster                                                |
| Geometric mean         | (ref)                                                                 | 1.08x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 16.0 ms                                                               | 15.9 ms: 1.00x faster                                                |
| mako            | 6.44 ms                                                               | 6.46 ms: 1.00x slower                                                |
| genshi_xml      | 39.7 ms                                                               | 40.3 ms: 1.01x slower                                                |
| django_template | 21.3 ms                                                               | 21.9 ms: 1.03x slower                                                |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                         |

All benchmarks:
===============

| Benchmark               | bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site  | 13.5 ms                                                               | 12.3 ms: 1.09x faster                                                |
| python_startup          | 16.0 ms                                                               | 14.9 ms: 1.07x faster                                                |
| richards                | 31.5 ms                                                               | 30.4 ms: 1.04x faster                                                |
| richards_super          | 35.4 ms                                                               | 34.3 ms: 1.03x faster                                                |
| bench_mp_pool           | 50.1 ms                                                               | 48.7 ms: 1.03x faster                                                |
| generators              | 23.7 ms                                                               | 23.2 ms: 1.03x faster                                                |
| nqueens                 | 58.4 ms                                                               | 57.3 ms: 1.02x faster                                                |
| raytrace                | 164 ms                                                                | 162 ms: 1.01x faster                                                 |
| 2to3                    | 171 ms                                                                | 170 ms: 1.01x faster                                                 |
| create_gc_cycles        | 903 us                                                                | 894 us: 1.01x faster                                                 |
| chaos                   | 39.3 ms                                                               | 39.0 ms: 1.01x faster                                                |
| coroutines              | 16.1 ms                                                               | 16.0 ms: 1.01x faster                                                |
| scimark_sparse_mat_mult | 2.95 ms                                                               | 2.92 ms: 1.01x faster                                                |
| asyncio_tcp_ssl         | 1.30 sec                                                              | 1.29 sec: 1.01x faster                                               |
| scimark_monte_carlo     | 43.9 ms                                                               | 43.6 ms: 1.01x faster                                                |
| sqlglot_transpile       | 1000 us                                                               | 994 us: 1.01x faster                                                 |
| pickle                  | 7.54 us                                                               | 7.49 us: 1.01x faster                                                |
| json_dumps              | 6.29 ms                                                               | 6.26 ms: 1.00x faster                                                |
| hexiom                  | 4.46 ms                                                               | 4.44 ms: 1.00x faster                                                |
| float                   | 46.6 ms                                                               | 46.4 ms: 1.00x faster                                                |
| mdp                     | 1.44 sec                                                              | 1.44 sec: 1.00x faster                                               |
| async_generators        | 295 ms                                                                | 294 ms: 1.00x faster                                                 |
| genshi_text             | 16.0 ms                                                               | 15.9 ms: 1.00x faster                                                |
| telco                   | 4.57 ms                                                               | 4.55 ms: 1.00x faster                                                |
| bpe_tokeniser           | 3.12 sec                                                              | 3.12 sec: 1.00x faster                                               |
| crypto_pyaes            | 51.7 ms                                                               | 51.5 ms: 1.00x faster                                                |
| html5lib                | 30.8 ms                                                               | 30.7 ms: 1.00x faster                                                |
| go                      | 101 ms                                                                | 101 ms: 1.00x faster                                                 |
| regex_dna               | 149 ms                                                                | 149 ms: 1.00x slower                                                 |
| regex_effbot            | 2.56 ms                                                               | 2.56 ms: 1.00x slower                                                |
| logging_simple          | 3.00 us                                                               | 3.01 us: 1.00x slower                                                |
| scimark_sor             | 102 ms                                                                | 102 ms: 1.00x slower                                                 |
| sqlite_synth            | 1.56 us                                                               | 1.57 us: 1.00x slower                                                |
| meteor_contest          | 71.8 ms                                                               | 72.1 ms: 1.00x slower                                                |
| mako                    | 6.44 ms                                                               | 6.46 ms: 1.00x slower                                                |
| pyflate                 | 315 ms                                                                | 316 ms: 1.00x slower                                                 |
| nbody                   | 63.5 ms                                                               | 63.6 ms: 1.00x slower                                                |
| async_tree_eager        | 63.2 ms                                                               | 63.4 ms: 1.00x slower                                                |
| sqlglot_normalize       | 176 ms                                                                | 177 ms: 1.00x slower                                                 |
| comprehensions          | 12.3 us                                                               | 12.3 us: 1.01x slower                                                |
| sqlglot_parse           | 823 us                                                                | 827 us: 1.01x slower                                                 |
| sqlglot_optimize        | 32.9 ms                                                               | 33.1 ms: 1.01x slower                                                |
| xml_etree_process       | 35.9 ms                                                               | 36.1 ms: 1.01x slower                                                |
| coverage                | 46.1 ms                                                               | 46.3 ms: 1.01x slower                                                |
| unpickle_pure_python    | 131 us                                                                | 132 us: 1.01x slower                                                 |
| logging_format          | 3.28 us                                                               | 3.30 us: 1.01x slower                                                |
| async_tree_eager_tg     | 42.0 ms                                                               | 42.3 ms: 1.01x slower                                                |
| scimark_fft             | 185 ms                                                                | 187 ms: 1.01x slower                                                 |
| unpickle_list           | 2.91 us                                                               | 2.93 us: 1.01x slower                                                |
| logging_silent          | 62.0 ns                                                               | 62.5 ns: 1.01x slower                                                |
| thrift                  | 434 us                                                                | 438 us: 1.01x slower                                                 |
| pickle_list             | 2.98 us                                                               | 3.02 us: 1.01x slower                                                |
| fannkuch                | 241 ms                                                                | 244 ms: 1.01x slower                                                 |
| pprint_safe_repr        | 469 ms                                                                | 475 ms: 1.01x slower                                                 |
| pidigits                | 282 ms                                                                | 286 ms: 1.01x slower                                                 |
| deepcopy_reduce         | 1.52 us                                                               | 1.55 us: 1.01x slower                                                |
| pprint_pformat          | 962 ms                                                                | 976 ms: 1.01x slower                                                 |
| genshi_xml              | 39.7 ms                                                               | 40.3 ms: 1.01x slower                                                |
| pickle_dict             | 18.3 us                                                               | 18.6 us: 1.02x slower                                                |
| pickle_pure_python      | 173 us                                                                | 176 us: 1.02x slower                                                 |
| json                    | 2.90 ms                                                               | 2.94 ms: 1.02x slower                                                |
| tomli_loads             | 1.25 sec                                                              | 1.27 sec: 1.02x slower                                               |
| xml_etree_generate      | 51.2 ms                                                               | 52.2 ms: 1.02x slower                                                |
| scimark_lu              | 78.9 ms                                                               | 80.8 ms: 1.02x slower                                                |
| django_template         | 21.3 ms                                                               | 21.9 ms: 1.03x slower                                                |
| deepcopy                | 151 us                                                                | 155 us: 1.03x slower                                                 |
| pathlib                 | 22.6 ms                                                               | 23.5 ms: 1.04x slower                                                |
| Geometric mean          | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (37): asyncio_tcp, tornado_http, unpickle, async_tree_eager_cpu_io_mixed, spectral_norm, sympy_str, async_tree_eager_io_tg, docutils, async_tree_io_tg, asyncio_websockets, typing_runtime_protocols, sympy_expand, async_tree_eager_cpu_io_mixed_tg, bench_thread_pool, xml_etree_parse, sympy_integrate, gc_traversal, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, regex_v8, deltablue, async_tree_eager_memoization_tg, async_tree_none, regex_compile, async_tree_eager_io, pycparser, async_tree_none_tg, async_tree_eager_memoization, json_loads, async_tree_memoization, async_tree_memoization_tg, deepcopy_memo, sympy_sum, xml_etree_iterparse, async_tree_io, pylint, dask

# HPT report

- Reliability score: 63.45% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.90x