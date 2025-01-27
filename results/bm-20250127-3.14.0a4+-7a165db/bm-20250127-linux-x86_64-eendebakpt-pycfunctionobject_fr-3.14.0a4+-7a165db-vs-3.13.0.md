# Results vs. 3.13.0

- fork: eendebakpt
- ref: pycfunctionobject_fr
- machine: linux-x86_64
- commit hash: 7a165db
- commit date: 2025-01-27
- overall geometric mean: 1.040x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4+-7a165db |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 255 ms: 1.04x faster                                                       |
| html5lib       | 63.4 ms                                                | 61.4 ms: 1.03x faster                                                      |
| sphinx         | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4+-7a165db |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.46x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                       |
| async_tree_io              | 838 ms                                                 | 621 ms: 1.35x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 324 ms: 1.35x faster                                                       |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                       |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.16x faster                                                       |
| async_generators           | 433 ms                                                 | 385 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 485 ms: 1.12x faster                                                       |
| coroutines                 | 22.2 ms                                                | 23.9 ms: 1.08x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4+-7a165db |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 73.6 ms: 1.07x faster                                                      |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                       |
| nbody          | 87.7 ms                                                | 98.2 ms: 1.12x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4+-7a165db |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.27 ms: 1.15x faster                                                      |
| regex_v8       | 26.9 ms                                                | 24.7 ms: 1.09x faster                                                      |
| regex_dna      | 220 ms                                                 | 209 ms: 1.05x faster                                                       |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4+-7a165db |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 140 ms: 1.10x faster                                                       |
| tomli_loads          | 2.12 sec                                               | 2.01 sec: 1.05x faster                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 98.2 ms: 1.03x faster                                                      |
| xml_etree_generate   | 86.8 ms                                                | 85.1 ms: 1.02x faster                                                      |
| xml_etree_process    | 60.5 ms                                                | 60.0 ms: 1.01x faster                                                      |
| unpickle_pure_python | 213 us                                                 | 219 us: 1.03x slower                                                       |
| json_loads           | 27.2 us                                                | 28.7 us: 1.06x slower                                                      |
| pickle_pure_python   | 302 us                                                 | 325 us: 1.07x slower                                                       |
| json_dumps           | 10.1 ms                                                | 11.7 ms: 1.16x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4+-7a165db |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.00 ms                                                | 7.07 ms: 1.01x slower                                                      |
| python_startup         | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4+-7a165db |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.4 ms: 1.06x faster                                                      |
| genshi_xml      | 50.5 ms                                                | 48.8 ms: 1.03x faster                                                      |
| django_template | 31.7 ms                                                | 32.4 ms: 1.02x slower                                                      |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250127-linux-x86_64-eendebakpt-pycfunctionobject_fr-3.14.0a4+-7a165db |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.46x faster                                                       |
| async_tree_io_tg           | 861 ms                                                 | 621 ms: 1.39x faster                                                       |
| deepcopy                   | 354 us                                                 | 256 us: 1.39x faster                                                       |
| async_tree_io              | 838 ms                                                 | 621 ms: 1.35x faster                                                       |
| async_tree_memoization     | 437 ms                                                 | 324 ms: 1.35x faster                                                       |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                       |
| async_tree_none_tg         | 319 ms                                                 | 256 ms: 1.25x faster                                                       |
| deepcopy_memo              | 38.4 us                                                | 31.3 us: 1.23x faster                                                      |
| deepcopy_reduce            | 3.24 us                                                | 2.66 us: 1.22x faster                                                      |
| go                         | 141 ms                                                 | 119 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 496 ms: 1.16x faster                                                       |
| regex_effbot               | 3.77 ms                                                | 3.27 ms: 1.15x faster                                                      |
| spectral_norm              | 113 ms                                                 | 99.8 ms: 1.13x faster                                                      |
| pylint                     | 312 ms                                                 | 275 ms: 1.13x faster                                                       |
| async_generators           | 433 ms                                                 | 385 ms: 1.13x faster                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 485 ms: 1.12x faster                                                       |
| pathlib                    | 17.4 ms                                                | 15.7 ms: 1.10x faster                                                      |
| xml_etree_parse            | 154 ms                                                 | 140 ms: 1.10x faster                                                       |
| regex_v8                   | 26.9 ms                                                | 24.7 ms: 1.09x faster                                                      |
| telco                      | 8.40 ms                                                | 7.76 ms: 1.08x faster                                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.70 ms: 1.07x faster                                                      |
| float                      | 78.7 ms                                                | 73.6 ms: 1.07x faster                                                      |
| richards                   | 47.5 ms                                                | 44.5 ms: 1.07x faster                                                      |
| richards_super             | 53.7 ms                                                | 50.4 ms: 1.07x faster                                                      |
| genshi_text                | 22.6 ms                                                | 21.4 ms: 1.06x faster                                                      |
| tomli_loads                | 2.12 sec                                               | 2.01 sec: 1.05x faster                                                     |
| sqlglot_normalize          | 108 ms                                                 | 103 ms: 1.05x faster                                                       |
| regex_dna                  | 220 ms                                                 | 209 ms: 1.05x faster                                                       |
| thrift                     | 800 us                                                 | 765 us: 1.05x faster                                                       |
| 2to3                       | 266 ms                                                 | 255 ms: 1.04x faster                                                       |
| sympy_str                  | 273 ms                                                 | 263 ms: 1.04x faster                                                       |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                       |
| sqlite_synth               | 2.90 us                                                | 2.80 us: 1.04x faster                                                      |
| logging_simple             | 5.65 us                                                | 5.46 us: 1.04x faster                                                      |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                                     |
| bpe_tokeniser              | 4.69 sec                                               | 4.53 sec: 1.03x faster                                                     |
| sympy_sum                  | 150 ms                                                 | 145 ms: 1.03x faster                                                       |
| sqlglot_optimize           | 53.4 ms                                                | 51.6 ms: 1.03x faster                                                      |
| genshi_xml                 | 50.5 ms                                                | 48.8 ms: 1.03x faster                                                      |
| html5lib                   | 63.4 ms                                                | 61.4 ms: 1.03x faster                                                      |
| json                       | 5.32 ms                                                | 5.16 ms: 1.03x faster                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 98.2 ms: 1.03x faster                                                      |
| k_core                     | 2.37 sec                                               | 2.30 sec: 1.03x faster                                                     |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                                       |
| sympy_expand               | 456 ms                                                 | 444 ms: 1.03x faster                                                       |
| sqlalchemy_imperative      | 16.9 ms                                                | 16.5 ms: 1.03x faster                                                      |
| logging_format             | 6.23 us                                                | 6.07 us: 1.03x faster                                                      |
| sphinx                     | 1.03 sec                                               | 1.00 sec: 1.03x faster                                                     |
| crypto_pyaes               | 74.7 ms                                                | 72.8 ms: 1.03x faster                                                      |
| xml_etree_generate         | 86.8 ms                                                | 85.1 ms: 1.02x faster                                                      |
| sympy_integrate            | 19.8 ms                                                | 19.5 ms: 1.02x faster                                                      |
| connected_components       | 447 ms                                                 | 440 ms: 1.02x faster                                                       |
| shortest_path              | 487 ms                                                 | 479 ms: 1.02x faster                                                       |
| mdp                        | 2.54 sec                                               | 2.50 sec: 1.02x faster                                                     |
| nqueens                    | 80.9 ms                                                | 79.8 ms: 1.01x faster                                                      |
| scimark_fft                | 367 ms                                                 | 362 ms: 1.01x faster                                                       |
| meteor_contest             | 108 ms                                                 | 107 ms: 1.01x faster                                                       |
| xml_etree_process          | 60.5 ms                                                | 60.0 ms: 1.01x faster                                                      |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                       |
| sqlglot_parse              | 1.26 ms                                                | 1.28 ms: 1.01x slower                                                      |
| create_gc_cycles           | 2.45 ms                                                | 2.47 ms: 1.01x slower                                                      |
| python_startup_no_site     | 7.00 ms                                                | 7.07 ms: 1.01x slower                                                      |
| gc_traversal               | 4.90 ms                                                | 4.95 ms: 1.01x slower                                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.59 ms: 1.01x slower                                                      |
| chaos                      | 58.0 ms                                                | 58.8 ms: 1.01x slower                                                      |
| python_startup             | 12.7 ms                                                | 12.8 ms: 1.01x slower                                                      |
| scimark_sor                | 122 ms                                                 | 124 ms: 1.02x slower                                                       |
| deltablue                  | 3.19 ms                                                | 3.26 ms: 1.02x slower                                                      |
| django_template            | 31.7 ms                                                | 32.4 ms: 1.02x slower                                                      |
| scimark_lu                 | 114 ms                                                 | 117 ms: 1.02x slower                                                       |
| scimark_monte_carlo        | 66.8 ms                                                | 68.7 ms: 1.03x slower                                                      |
| unpickle_pure_python       | 213 us                                                 | 219 us: 1.03x slower                                                       |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                                      |
| pyflate                    | 470 ms                                                 | 484 ms: 1.03x slower                                                       |
| fannkuch                   | 394 ms                                                 | 407 ms: 1.04x slower                                                       |
| hexiom                     | 6.08 ms                                                | 6.30 ms: 1.04x slower                                                      |
| raytrace                   | 262 ms                                                 | 274 ms: 1.05x slower                                                       |
| bench_thread_pool          | 818 us                                                 | 859 us: 1.05x slower                                                       |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                      |
| json_loads                 | 27.2 us                                                | 28.7 us: 1.06x slower                                                      |
| pickle_pure_python         | 302 us                                                 | 325 us: 1.07x slower                                                       |
| coroutines                 | 22.2 ms                                                | 23.9 ms: 1.08x slower                                                      |
| logging_silent             | 101 ns                                                 | 109 ns: 1.08x slower                                                       |
| many_optionals             | 857 us                                                 | 941 us: 1.10x slower                                                       |
| coverage                   | 82.8 ms                                                | 91.2 ms: 1.10x slower                                                      |
| nbody                      | 87.7 ms                                                | 98.2 ms: 1.12x slower                                                      |
| json_dumps                 | 10.1 ms                                                | 11.7 ms: 1.16x slower                                                      |
| subparsers                 | 15.5 ms                                                | 20.5 ms: 1.33x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 81.2 ms: 3.39x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (7): pprint_safe_repr, typing_runtime_protocols, pprint_pformat, dulwich_log, generators, docutils, asyncio_websockets
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.02x