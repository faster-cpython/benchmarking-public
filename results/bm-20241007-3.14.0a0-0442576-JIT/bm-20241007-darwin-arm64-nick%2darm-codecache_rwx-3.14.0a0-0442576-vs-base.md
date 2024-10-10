# Results vs. base

- fork: nick-arm
- ref: codecache_rwx
- machine: darwin-arm64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 180 ms                                                                | 168 ms: 1.07x faster                                               |
| docutils       | 1.57 sec                                                              | 1.49 sec: 1.05x faster                                             |
| html5lib       | 34.1 ms                                                               | 32.6 ms: 1.04x faster                                              |
| Geometric mean | (ref)                                                                 | 1.04x faster                                                       |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark           | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|---------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_eager    | 63.8 ms                                                               | 61.1 ms: 1.04x faster                                              |
| async_generators    | 292 ms                                                                | 289 ms: 1.01x faster                                               |
| async_tree_eager_tg | 41.6 ms                                                               | 41.2 ms: 1.01x faster                                              |
| coroutines          | 16.3 ms                                                               | 16.3 ms: 1.00x slower                                              |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (17): async_tree_eager_memoization, async_tree_eager_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_none, async_tree_none_tg, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_io, async_tree_memoization_tg, async_tree_eager_io_tg, async_tree_io_tg, asyncio_tcp, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| nbody          | 63.6 ms                                                               | 63.5 ms: 1.00x faster                                              |
| pidigits       | 283 ms                                                                | 283 ms: 1.00x slower                                               |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                       |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                               | 71.8 ms: 1.06x faster                                              |
| regex_dna      | 149 ms                                                                | 148 ms: 1.01x faster                                               |
| regex_effbot   | 2.63 ms                                                               | 2.61 ms: 1.01x faster                                              |
| regex_v8       | 16.8 ms                                                               | 17.0 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| xml_etree_process    | 34.4 ms                                                               | 33.8 ms: 1.02x faster                                              |
| pickle_list          | 2.97 us                                                               | 2.94 us: 1.01x faster                                              |
| xml_etree_generate   | 49.8 ms                                                               | 49.2 ms: 1.01x faster                                              |
| tomli_loads          | 1.25 sec                                                              | 1.24 sec: 1.01x faster                                             |
| json_loads           | 16.4 us                                                               | 16.3 us: 1.01x faster                                              |
| pickle_dict          | 18.2 us                                                               | 18.1 us: 1.01x faster                                              |
| xml_etree_iterparse  | 71.3 ms                                                               | 70.9 ms: 1.01x faster                                              |
| unpickle_pure_python | 131 us                                                                | 130 us: 1.00x faster                                               |
| pickle_pure_python   | 176 us                                                                | 175 us: 1.00x faster                                               |
| unpickle_list        | 2.97 us                                                               | 2.99 us: 1.01x slower                                              |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                       |

Benchmark hidden because not significant (4): xml_etree_parse, json_dumps, unpickle, pickle

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 42.8 ms                                                               | 31.8 ms: 1.34x faster                                              |
| genshi_text     | 17.1 ms                                                               | 14.6 ms: 1.17x faster                                              |
| django_template | 22.8 ms                                                               | 20.2 ms: 1.13x faster                                              |
| mako            | 6.41 ms                                                               | 6.39 ms: 1.00x faster                                              |
| Geometric mean  | (ref)                                                                 | 1.16x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20241004-darwin-arm64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 | bm-20241007-darwin-arm64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------:|
| richards                | 44.9 ms                                                               | 30.7 ms: 1.46x faster                                              |
| richards_super          | 46.4 ms                                                               | 34.1 ms: 1.36x faster                                              |
| genshi_xml              | 42.8 ms                                                               | 31.8 ms: 1.34x faster                                              |
| genshi_text             | 17.1 ms                                                               | 14.6 ms: 1.17x faster                                              |
| django_template         | 22.8 ms                                                               | 20.2 ms: 1.13x faster                                              |
| sqlglot_optimize        | 37.7 ms                                                               | 33.9 ms: 1.11x faster                                              |
| sqlglot_normalize       | 188 ms                                                                | 175 ms: 1.08x faster                                               |
| go                      | 100 ms                                                                | 93.4 ms: 1.08x faster                                              |
| 2to3                    | 180 ms                                                                | 168 ms: 1.07x faster                                               |
| sqlglot_transpile       | 1.05 ms                                                               | 986 us: 1.07x faster                                               |
| sympy_integrate         | 12.5 ms                                                               | 11.8 ms: 1.06x faster                                              |
| sympy_str               | 150 ms                                                                | 142 ms: 1.06x faster                                               |
| hexiom                  | 4.70 ms                                                               | 4.42 ms: 1.06x faster                                              |
| sympy_sum               | 78.7 ms                                                               | 74.5 ms: 1.06x faster                                              |
| sqlglot_parse           | 854 us                                                                | 808 us: 1.06x faster                                               |
| regex_compile           | 75.9 ms                                                               | 71.8 ms: 1.06x faster                                              |
| docutils                | 1.57 sec                                                              | 1.49 sec: 1.05x faster                                             |
| pprint_safe_repr        | 490 ms                                                                | 467 ms: 1.05x faster                                               |
| pycparser               | 680 ms                                                                | 649 ms: 1.05x faster                                               |
| sympy_expand            | 247 ms                                                                | 236 ms: 1.05x faster                                               |
| html5lib                | 34.1 ms                                                               | 32.6 ms: 1.04x faster                                              |
| async_tree_eager        | 63.8 ms                                                               | 61.1 ms: 1.04x faster                                              |
| generators              | 25.2 ms                                                               | 24.2 ms: 1.04x faster                                              |
| deepcopy                | 154 us                                                                | 148 us: 1.04x faster                                               |
| scimark_monte_carlo     | 47.7 ms                                                               | 46.2 ms: 1.03x faster                                              |
| meteor_contest          | 75.6 ms                                                               | 73.6 ms: 1.03x faster                                              |
| raytrace                | 176 ms                                                                | 171 ms: 1.03x faster                                               |
| logging_format          | 3.37 us                                                               | 3.30 us: 1.02x faster                                              |
| bench_mp_pool           | 51.9 ms                                                               | 50.7 ms: 1.02x faster                                              |
| fannkuch                | 265 ms                                                                | 260 ms: 1.02x faster                                               |
| chaos                   | 40.6 ms                                                               | 39.8 ms: 1.02x faster                                              |
| comprehensions          | 12.8 us                                                               | 12.5 us: 1.02x faster                                              |
| pyflate                 | 323 ms                                                                | 317 ms: 1.02x faster                                               |
| xml_etree_process       | 34.4 ms                                                               | 33.8 ms: 1.02x faster                                              |
| dulwich_log             | 29.2 ms                                                               | 28.7 ms: 1.02x faster                                              |
| mdp                     | 1.48 sec                                                              | 1.46 sec: 1.02x faster                                             |
| bench_thread_pool       | 483 us                                                                | 476 us: 1.01x faster                                               |
| json                    | 2.89 ms                                                               | 2.85 ms: 1.01x faster                                              |
| logging_simple          | 3.07 us                                                               | 3.03 us: 1.01x faster                                              |
| crypto_pyaes            | 52.6 ms                                                               | 52.0 ms: 1.01x faster                                              |
| pickle_list             | 2.97 us                                                               | 2.94 us: 1.01x faster                                              |
| xml_etree_generate      | 49.8 ms                                                               | 49.2 ms: 1.01x faster                                              |
| async_generators        | 292 ms                                                                | 289 ms: 1.01x faster                                               |
| tomli_loads             | 1.25 sec                                                              | 1.24 sec: 1.01x faster                                             |
| unpack_sequence         | 76.0 ns                                                               | 75.1 ns: 1.01x faster                                              |
| json_loads              | 16.4 us                                                               | 16.3 us: 1.01x faster                                              |
| async_tree_eager_tg     | 41.6 ms                                                               | 41.2 ms: 1.01x faster                                              |
| deltablue               | 2.38 ms                                                               | 2.36 ms: 1.01x faster                                              |
| sqlite_synth            | 1.55 us                                                               | 1.53 us: 1.01x faster                                              |
| regex_dna               | 149 ms                                                                | 148 ms: 1.01x faster                                               |
| thrift                  | 420 us                                                                | 417 us: 1.01x faster                                               |
| regex_effbot            | 2.63 ms                                                               | 2.61 ms: 1.01x faster                                              |
| coverage                | 43.8 ms                                                               | 43.6 ms: 1.01x faster                                              |
| pickle_dict             | 18.2 us                                                               | 18.1 us: 1.01x faster                                              |
| deepcopy_memo           | 16.3 us                                                               | 16.2 us: 1.01x faster                                              |
| pprint_pformat          | 990 ms                                                                | 985 ms: 1.01x faster                                               |
| xml_etree_iterparse     | 71.3 ms                                                               | 70.9 ms: 1.01x faster                                              |
| unpickle_pure_python    | 131 us                                                                | 130 us: 1.00x faster                                               |
| scimark_fft             | 185 ms                                                                | 184 ms: 1.00x faster                                               |
| pickle_pure_python      | 176 us                                                                | 175 us: 1.00x faster                                               |
| mako                    | 6.41 ms                                                               | 6.39 ms: 1.00x faster                                              |
| nbody                   | 63.6 ms                                                               | 63.5 ms: 1.00x faster                                              |
| scimark_lu              | 64.2 ms                                                               | 64.1 ms: 1.00x faster                                              |
| pidigits                | 283 ms                                                                | 283 ms: 1.00x slower                                               |
| spectral_norm           | 66.8 ms                                                               | 66.9 ms: 1.00x slower                                              |
| scimark_sor             | 87.2 ms                                                               | 87.4 ms: 1.00x slower                                              |
| coroutines              | 16.3 ms                                                               | 16.3 ms: 1.00x slower                                              |
| telco                   | 4.54 ms                                                               | 4.57 ms: 1.01x slower                                              |
| scimark_sparse_mat_mult | 2.97 ms                                                               | 2.99 ms: 1.01x slower                                              |
| unpickle_list           | 2.97 us                                                               | 2.99 us: 1.01x slower                                              |
| regex_v8                | 16.8 ms                                                               | 17.0 ms: 1.01x slower                                              |
| Geometric mean          | (ref)                                                                 | 1.03x faster                                                       |

Benchmark hidden because not significant (34): pylint, xml_etree_parse, async_tree_eager_memoization, async_tree_eager_cpu_io_mixed, async_tree_eager_memoization_tg, async_tree_none, async_tree_none_tg, async_tree_io, deepcopy_reduce, nqueens, async_tree_memoization, async_tree_cpu_io_mixed, tornado_http, float, python_startup, python_startup_no_site, asyncio_websockets, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed_tg, json_dumps, unpickle, bpe_tokeniser, gc_traversal, async_tree_eager_io, async_tree_memoization_tg, create_gc_cycles, logging_silent, async_tree_eager_io_tg, pathlib, async_tree_io_tg, asyncio_tcp, typing_runtime_protocols, pickle, asyncio_tcp_ssl

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x