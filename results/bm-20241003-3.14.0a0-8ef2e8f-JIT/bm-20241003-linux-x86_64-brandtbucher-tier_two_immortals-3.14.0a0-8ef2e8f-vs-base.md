# Results vs. base

- fork: brandtbucher
- ref: tier_two_immortals
- machine: linux-x86_64
- commit hash: 8ef2e8f
- commit date: 2024-10-03
- overall geometric mean: 1.00x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                                | 279 ms: 1.00x faster                                                      |
| html5lib       | 65.5 ms                                                               | 64.7 ms: 1.01x faster                                                     |
| tornado_http   | 95.4 ms                                                               | 94.9 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                              |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| coroutines             | 23.2 ms                                                               | 22.4 ms: 1.03x faster                                                     |
| async_tree_memoization | 412 ms                                                                | 408 ms: 1.01x faster                                                      |
| asyncio_tcp            | 488 ms                                                                | 484 ms: 1.01x faster                                                      |
| async_generators       | 453 ms                                                                | 452 ms: 1.00x faster                                                      |
| asyncio_tcp_ssl        | 1.79 sec                                                              | 1.79 sec: 1.00x slower                                                    |
| asyncio_websockets     | 555 ms                                                                | 558 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                              |

Benchmark hidden because not significant (7): async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 72.0 ms                                                               | 71.8 ms: 1.00x faster                                                     |
| pidigits       | 186 ms                                                                | 185 ms: 1.00x faster                                                      |
| nbody          | 80.7 ms                                                               | 82.3 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.79 ms                                                               | 3.69 ms: 1.03x faster                                                     |
| regex_compile  | 145 ms                                                                | 143 ms: 1.02x faster                                                      |
| regex_dna      | 218 ms                                                                | 221 ms: 1.01x slower                                                      |
| regex_v8       | 24.6 ms                                                               | 25.5 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_list        | 5.44 us                                                               | 5.16 us: 1.05x faster                                                     |
| tomli_loads          | 1.93 sec                                                              | 1.90 sec: 1.01x faster                                                    |
| xml_etree_process    | 54.9 ms                                                               | 54.4 ms: 1.01x faster                                                     |
| pickle_dict          | 34.7 us                                                               | 34.4 us: 1.01x faster                                                     |
| unpickle_pure_python | 214 us                                                                | 213 us: 1.01x faster                                                      |
| pickle               | 11.4 us                                                               | 11.4 us: 1.01x faster                                                     |
| xml_etree_generate   | 77.2 ms                                                               | 76.8 ms: 1.01x faster                                                     |
| xml_etree_iterparse  | 97.8 ms                                                               | 98.1 ms: 1.00x slower                                                     |
| json_loads           | 26.6 us                                                               | 26.9 us: 1.01x slower                                                     |
| pickle_pure_python   | 306 us                                                                | 309 us: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                              |

Benchmark hidden because not significant (4): unpickle, xml_etree_parse, pickle_list, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.01x faster                                                     |
| python_startup_no_site | 7.07 ms                                                               | 7.03 ms: 1.01x faster                                                     |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                               | 57.9 ms: 1.01x slower                                                     |
| mako            | 9.80 ms                                                               | 9.90 ms: 1.01x slower                                                     |
| django_template | 36.3 ms                                                               | 36.9 ms: 1.02x slower                                                     |
| genshi_text     | 24.7 ms                                                               | 25.5 ms: 1.03x slower                                                     |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                              |

All benchmarks:
===============

| Benchmark               | bm-20240929-linux-x86_64-python-6f4d64b048133c60d407-3.14.0a0-6f4d64b | bm-20241003-linux-x86_64-brandtbucher-tier_two_immortals-3.14.0a0-8ef2e8f |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_list           | 5.44 us                                                               | 5.16 us: 1.05x faster                                                     |
| scimark_sparse_mat_mult | 4.55 ms                                                               | 4.36 ms: 1.04x faster                                                     |
| pyflate                 | 450 ms                                                                | 435 ms: 1.04x faster                                                      |
| coroutines              | 23.2 ms                                                               | 22.4 ms: 1.03x faster                                                     |
| scimark_fft             | 317 ms                                                                | 307 ms: 1.03x faster                                                      |
| spectral_norm           | 103 ms                                                                | 100 ms: 1.03x faster                                                      |
| regex_effbot            | 3.79 ms                                                               | 3.69 ms: 1.03x faster                                                     |
| regex_compile           | 145 ms                                                                | 143 ms: 1.02x faster                                                      |
| sympy_str               | 308 ms                                                                | 303 ms: 1.02x faster                                                      |
| unpack_sequence         | 110 ns                                                                | 108 ns: 1.02x faster                                                      |
| sympy_sum               | 177 ms                                                                | 175 ms: 1.01x faster                                                      |
| richards_super          | 45.3 ms                                                               | 44.7 ms: 1.01x faster                                                     |
| dulwich_log             | 69.0 ms                                                               | 68.2 ms: 1.01x faster                                                     |
| sympy_expand            | 511 ms                                                                | 505 ms: 1.01x faster                                                      |
| tomli_loads             | 1.93 sec                                                              | 1.90 sec: 1.01x faster                                                    |
| bench_mp_pool           | 60.9 ms                                                               | 60.2 ms: 1.01x faster                                                     |
| html5lib                | 65.5 ms                                                               | 64.7 ms: 1.01x faster                                                     |
| async_tree_memoization  | 412 ms                                                                | 408 ms: 1.01x faster                                                      |
| generators              | 34.8 ms                                                               | 34.5 ms: 1.01x faster                                                     |
| sqlglot_normalize       | 116 ms                                                                | 114 ms: 1.01x faster                                                      |
| sqlglot_transpile       | 1.70 ms                                                               | 1.68 ms: 1.01x faster                                                     |
| telco                   | 7.55 ms                                                               | 7.49 ms: 1.01x faster                                                     |
| xml_etree_process       | 54.9 ms                                                               | 54.4 ms: 1.01x faster                                                     |
| asyncio_tcp             | 488 ms                                                                | 484 ms: 1.01x faster                                                      |
| pickle_dict             | 34.7 us                                                               | 34.4 us: 1.01x faster                                                     |
| crypto_pyaes            | 65.9 ms                                                               | 65.4 ms: 1.01x faster                                                     |
| unpickle_pure_python    | 214 us                                                                | 213 us: 1.01x faster                                                      |
| mdp                     | 2.56 sec                                                              | 2.54 sec: 1.01x faster                                                    |
| pickle                  | 11.4 us                                                               | 11.4 us: 1.01x faster                                                     |
| python_startup          | 10.5 ms                                                               | 10.5 ms: 1.01x faster                                                     |
| tornado_http            | 95.4 ms                                                               | 94.9 ms: 1.01x faster                                                     |
| pathlib                 | 15.7 ms                                                               | 15.6 ms: 1.01x faster                                                     |
| python_startup_no_site  | 7.07 ms                                                               | 7.03 ms: 1.01x faster                                                     |
| xml_etree_generate      | 77.2 ms                                                               | 76.8 ms: 1.01x faster                                                     |
| async_generators        | 453 ms                                                                | 452 ms: 1.00x faster                                                      |
| bpe_tokeniser           | 4.44 sec                                                              | 4.43 sec: 1.00x faster                                                    |
| float                   | 72.0 ms                                                               | 71.8 ms: 1.00x faster                                                     |
| 2to3                    | 280 ms                                                                | 279 ms: 1.00x faster                                                      |
| sympy_integrate         | 23.5 ms                                                               | 23.4 ms: 1.00x faster                                                     |
| pidigits                | 186 ms                                                                | 185 ms: 1.00x faster                                                      |
| create_gc_cycles        | 1.74 ms                                                               | 1.73 ms: 1.00x faster                                                     |
| asyncio_tcp_ssl         | 1.79 sec                                                              | 1.79 sec: 1.00x slower                                                    |
| gc_traversal            | 3.84 ms                                                               | 3.85 ms: 1.00x slower                                                     |
| xml_etree_iterparse     | 97.8 ms                                                               | 98.1 ms: 1.00x slower                                                     |
| hexiom                  | 6.93 ms                                                               | 6.95 ms: 1.00x slower                                                     |
| meteor_contest          | 107 ms                                                                | 107 ms: 1.00x slower                                                      |
| asyncio_websockets      | 555 ms                                                                | 558 ms: 1.01x slower                                                      |
| bench_thread_pool       | 891 us                                                                | 896 us: 1.01x slower                                                      |
| thrift                  | 792 us                                                                | 797 us: 1.01x slower                                                      |
| json                    | 5.02 ms                                                               | 5.06 ms: 1.01x slower                                                     |
| go                      | 131 ms                                                                | 132 ms: 1.01x slower                                                      |
| raytrace                | 276 ms                                                                | 278 ms: 1.01x slower                                                      |
| genshi_xml              | 57.3 ms                                                               | 57.9 ms: 1.01x slower                                                     |
| nqueens                 | 85.1 ms                                                               | 85.9 ms: 1.01x slower                                                     |
| json_loads              | 26.6 us                                                               | 26.9 us: 1.01x slower                                                     |
| mako                    | 9.80 ms                                                               | 9.90 ms: 1.01x slower                                                     |
| deepcopy                | 268 us                                                                | 271 us: 1.01x slower                                                      |
| pickle_pure_python      | 306 us                                                                | 309 us: 1.01x slower                                                      |
| regex_dna               | 218 ms                                                                | 221 ms: 1.01x slower                                                      |
| sqlite_synth            | 2.72 us                                                               | 2.76 us: 1.02x slower                                                     |
| django_template         | 36.3 ms                                                               | 36.9 ms: 1.02x slower                                                     |
| nbody                   | 80.7 ms                                                               | 82.3 ms: 1.02x slower                                                     |
| logging_simple          | 5.54 us                                                               | 5.67 us: 1.02x slower                                                     |
| logging_format          | 6.12 us                                                               | 6.28 us: 1.03x slower                                                     |
| genshi_text             | 24.7 ms                                                               | 25.5 ms: 1.03x slower                                                     |
| pycparser               | 1.16 sec                                                              | 1.20 sec: 1.03x slower                                                    |
| regex_v8                | 24.6 ms                                                               | 25.5 ms: 1.04x slower                                                     |
| Geometric mean          | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (30): unpickle, async_tree_none, scimark_sor, deepcopy_reduce, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_none_tg, logging_silent, async_tree_memoization_tg, deltablue, async_tree_io, scimark_monte_carlo, richards, comprehensions, xml_etree_parse, typing_runtime_protocols, pickle_list, sqlglot_parse, fannkuch, docutils, coverage, deepcopy_memo, sqlglot_optimize, scimark_lu, pylint, chaos, pprint_safe_repr, json_dumps, pprint_pformat

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x