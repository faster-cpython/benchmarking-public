# Results vs. base

- fork: eendebakpt
- ref: pycfunctionobject_fr
- machine: linux-x86_64
- commit hash: 7a165db
- commit date: 2025-01-27
- overall geometric mean: 1.003x faster
- HPT reliability: 97.49%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250127-linux-x86_64-python-7ec17429d462aee071c0-3.14.0a4+-7ec1742 | bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4+-7a165db |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                 | 255 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250127-linux-x86_64-python-7ec17429d462aee071c0-3.14.0a4+-7ec1742 | bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4+-7a165db |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none         | 267 ms                                                                 | 264 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed | 500 ms                                                                 | 496 ms: 1.01x faster                                                       |
| async_tree_memoization  | 326 ms                                                                 | 324 ms: 1.01x faster                                                       |
| async_generators        | 387 ms                                                                 | 385 ms: 1.01x faster                                                       |
| async_tree_io_tg        | 610 ms                                                                 | 621 ms: 1.02x slower                                                       |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_none_tg, asyncio_websockets, coroutines, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250127-linux-x86_64-python-7ec17429d462aee071c0-3.14.0a4+-7ec1742 | bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4+-7a165db |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 98.7 ms                                                                | 98.2 ms: 1.00x faster                                                      |
| pidigits       | 186 ms                                                                 | 187 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250127-linux-x86_64-python-7ec17429d462aee071c0-3.14.0a4+-7ec1742 | bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4+-7a165db |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 25.7 ms                                                                | 24.7 ms: 1.04x faster                                                      |
| regex_effbot   | 3.32 ms                                                                | 3.27 ms: 1.01x faster                                                      |
| regex_compile  | 128 ms                                                                 | 127 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250127-linux-x86_64-python-7ec17429d462aee071c0-3.14.0a4+-7ec1742 | bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4+-7a165db |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 2.03 sec                                                               | 2.01 sec: 1.01x faster                                                     |
| unpickle_pure_python | 221 us                                                                 | 219 us: 1.01x faster                                                       |
| xml_etree_process    | 59.7 ms                                                                | 60.0 ms: 1.00x slower                                                      |
| json_dumps           | 11.6 ms                                                                | 11.7 ms: 1.01x slower                                                      |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (5): json_loads, pickle_pure_python, xml_etree_iterparse, xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250127-linux-x86_64-python-7ec17429d462aee071c0-3.14.0a4+-7ec1742 | bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4+-7a165db |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                      |
| python_startup_no_site | 7.04 ms                                                                | 7.07 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250127-linux-x86_64-python-7ec17429d462aee071c0-3.14.0a4+-7ec1742 | bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4+-7a165db |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako           | 11.8 ms                                                                | 11.3 ms: 1.04x faster                                                      |
| genshi_text    | 21.6 ms                                                                | 21.4 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                               |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20250127-linux-x86_64-python-7ec17429d462aee071c0-3.14.0a4+-7ec1742 | bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4+-7a165db |
|-------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako                    | 11.8 ms                                                                | 11.3 ms: 1.04x faster                                                      |
| regex_v8                | 25.7 ms                                                                | 24.7 ms: 1.04x faster                                                      |
| scimark_sparse_mat_mult | 4.81 ms                                                                | 4.70 ms: 1.02x faster                                                      |
| logging_simple          | 5.59 us                                                                | 5.46 us: 1.02x faster                                                      |
| sympy_expand            | 452 ms                                                                 | 444 ms: 1.02x faster                                                       |
| pathlib                 | 16.0 ms                                                                | 15.7 ms: 1.02x faster                                                      |
| sympy_integrate         | 19.8 ms                                                                | 19.5 ms: 1.02x faster                                                      |
| hexiom                  | 6.41 ms                                                                | 6.30 ms: 1.02x faster                                                      |
| crypto_pyaes            | 73.9 ms                                                                | 72.8 ms: 1.02x faster                                                      |
| sqlglot_optimize        | 52.4 ms                                                                | 51.6 ms: 1.02x faster                                                      |
| regex_effbot            | 3.32 ms                                                                | 3.27 ms: 1.01x faster                                                      |
| richards_super          | 51.1 ms                                                                | 50.4 ms: 1.01x faster                                                      |
| sqlglot_normalize       | 104 ms                                                                 | 103 ms: 1.01x faster                                                       |
| deltablue               | 3.30 ms                                                                | 3.26 ms: 1.01x faster                                                      |
| sympy_str               | 266 ms                                                                 | 263 ms: 1.01x faster                                                       |
| genshi_text             | 21.6 ms                                                                | 21.4 ms: 1.01x faster                                                      |
| async_tree_none         | 267 ms                                                                 | 264 ms: 1.01x faster                                                       |
| scimark_lu              | 118 ms                                                                 | 117 ms: 1.01x faster                                                       |
| sympy_sum               | 147 ms                                                                 | 145 ms: 1.01x faster                                                       |
| tomli_loads             | 2.03 sec                                                               | 2.01 sec: 1.01x faster                                                     |
| deepcopy_reduce         | 2.68 us                                                                | 2.66 us: 1.01x faster                                                      |
| pprint_pformat          | 1.49 sec                                                               | 1.47 sec: 1.01x faster                                                     |
| async_tree_cpu_io_mixed | 500 ms                                                                 | 496 ms: 1.01x faster                                                       |
| logging_format          | 6.12 us                                                                | 6.07 us: 1.01x faster                                                      |
| bench_thread_pool       | 867 us                                                                 | 859 us: 1.01x faster                                                       |
| regex_compile           | 128 ms                                                                 | 127 ms: 1.01x faster                                                       |
| async_tree_memoization  | 326 ms                                                                 | 324 ms: 1.01x faster                                                       |
| deepcopy                | 257 us                                                                 | 256 us: 1.01x faster                                                       |
| thrift                  | 770 us                                                                 | 765 us: 1.01x faster                                                       |
| unpickle_pure_python    | 221 us                                                                 | 219 us: 1.01x faster                                                       |
| async_generators        | 387 ms                                                                 | 385 ms: 1.01x faster                                                       |
| nbody                   | 98.7 ms                                                                | 98.2 ms: 1.00x faster                                                      |
| raytrace                | 275 ms                                                                 | 274 ms: 1.00x faster                                                       |
| bpe_tokeniser           | 4.55 sec                                                               | 4.53 sec: 1.00x faster                                                     |
| sqlglot_parse           | 1.28 ms                                                                | 1.28 ms: 1.00x faster                                                      |
| nqueens                 | 80.1 ms                                                                | 79.8 ms: 1.00x faster                                                      |
| fannkuch                | 409 ms                                                                 | 407 ms: 1.00x faster                                                       |
| generators              | 28.8 ms                                                                | 28.7 ms: 1.00x faster                                                      |
| python_startup          | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                      |
| mdp                     | 2.50 sec                                                               | 2.50 sec: 1.00x slower                                                     |
| deepcopy_memo           | 31.2 us                                                                | 31.3 us: 1.00x slower                                                      |
| pidigits                | 186 ms                                                                 | 187 ms: 1.00x slower                                                       |
| xml_etree_process       | 59.7 ms                                                                | 60.0 ms: 1.00x slower                                                      |
| many_optionals          | 937 us                                                                 | 941 us: 1.00x slower                                                       |
| python_startup_no_site  | 7.04 ms                                                                | 7.07 ms: 1.00x slower                                                      |
| 2to3                    | 254 ms                                                                 | 255 ms: 1.00x slower                                                       |
| json_dumps              | 11.6 ms                                                                | 11.7 ms: 1.01x slower                                                      |
| scimark_monte_carlo     | 68.2 ms                                                                | 68.7 ms: 1.01x slower                                                      |
| comprehensions          | 16.9 us                                                                | 17.0 us: 1.01x slower                                                      |
| spectral_norm           | 99.1 ms                                                                | 99.8 ms: 1.01x slower                                                      |
| dulwich_log             | 64.0 ms                                                                | 64.5 ms: 1.01x slower                                                      |
| create_gc_cycles        | 2.45 ms                                                                | 2.47 ms: 1.01x slower                                                      |
| logging_silent          | 108 ns                                                                 | 109 ns: 1.01x slower                                                       |
| meteor_contest          | 106 ms                                                                 | 107 ms: 1.01x slower                                                       |
| sqlite_synth            | 2.77 us                                                                | 2.80 us: 1.01x slower                                                      |
| async_tree_io_tg        | 610 ms                                                                 | 621 ms: 1.02x slower                                                       |
| scimark_fft             | 355 ms                                                                 | 362 ms: 1.02x slower                                                       |
| gc_traversal            | 4.85 ms                                                                | 4.95 ms: 1.02x slower                                                      |
| pyflate                 | 457 ms                                                                 | 484 ms: 1.06x slower                                                       |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (37): pycparser, json, pprint_safe_repr, async_tree_cpu_io_mixed_tg, sphinx, richards, docutils, django_template, json_loads, chaos, scimark_sor, go, sqlalchemy_imperative, pickle_pure_python, regex_dna, xml_etree_iterparse, coverage, sqlglot_transpile, async_tree_io, bench_mp_pool, async_tree_none_tg, pylint, asyncio_websockets, sqlalchemy_declarative, coroutines, telco, xml_etree_generate, subparsers, xml_etree_parse, k_core, genshi_xml, shortest_path, html5lib, typing_runtime_protocols, float, connected_components, async_tree_memoization_tg

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 97.49% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x