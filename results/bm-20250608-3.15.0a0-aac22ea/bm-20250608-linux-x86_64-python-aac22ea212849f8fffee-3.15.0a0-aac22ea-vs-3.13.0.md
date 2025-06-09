# Results vs. 3.13.0

- fork: python
- ref: aac22ea212849f8fffee
- machine: linux-x86_64
- commit hash: aac22ea
- commit date: 2025-06-08
- overall geometric mean: 1.042x slower
- HPT reliability: 97.79%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 266 ms                                                 | 256 ms: 1.04x faster                                                  |
| html5lib       | 63.4 ms                                                | 62.0 ms: 1.02x faster                                                 |
| sphinx         | 1.03 sec                                               | 1.02 sec: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.46x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                                  |
| async_tree_io              | 838 ms                                                 | 603 ms: 1.39x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                                  |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                  |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 508 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 499 ms: 1.09x faster                                                  |
| async_generators           | 433 ms                                                 | 409 ms: 1.06x faster                                                  |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.12x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.20x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 78.7 ms                                                | 71.5 ms: 1.10x faster                                                 |
| pidigits       | 186 ms                                                 | 192 ms: 1.03x slower                                                  |
| nbody          | 87.7 ms                                                | 102 ms: 1.16x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.77 ms                                                | 3.25 ms: 1.16x faster                                                 |
| regex_v8       | 26.9 ms                                                | 23.3 ms: 1.15x faster                                                 |
| regex_dna      | 220 ms                                                 | 210 ms: 1.05x faster                                                  |
| regex_compile  | 132 ms                                                 | 127 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                 | 144 ms: 1.07x faster                                                  |
| tomli_loads          | 2.12 sec                                               | 2.06 sec: 1.03x faster                                                |
| xml_etree_iterparse  | 101 ms                                                 | 99.7 ms: 1.02x faster                                                 |
| xml_etree_generate   | 86.8 ms                                                | 85.9 ms: 1.01x faster                                                 |
| xml_etree_process    | 60.5 ms                                                | 61.0 ms: 1.01x slower                                                 |
| unpickle_pure_python | 213 us                                                 | 219 us: 1.03x slower                                                  |
| json_loads           | 27.2 us                                                | 28.5 us: 1.05x slower                                                 |
| pickle_pure_python   | 302 us                                                 | 321 us: 1.06x slower                                                  |
| json_dumps           | 10.1 ms                                                | 11.1 ms: 1.10x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                 |
| python_startup_no_site | 7.00 ms                                                | 6.90 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                | 21.8 ms: 1.04x faster                                                 |
| genshi_xml      | 50.5 ms                                                | 49.9 ms: 1.01x faster                                                 |
| django_template | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                 |
| mako            | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.54 sec                                               | 1.22 sec: 2.08x faster                                                |
| async_tree_memoization_tg  | 463 ms                                                 | 318 ms: 1.46x faster                                                  |
| async_tree_io_tg           | 861 ms                                                 | 616 ms: 1.40x faster                                                  |
| async_tree_io              | 838 ms                                                 | 603 ms: 1.39x faster                                                  |
| deepcopy                   | 354 us                                                 | 256 us: 1.38x faster                                                  |
| async_tree_memoization     | 437 ms                                                 | 317 ms: 1.38x faster                                                  |
| async_tree_none            | 350 ms                                                 | 264 ms: 1.33x faster                                                  |
| deepcopy_memo              | 38.4 us                                                | 29.2 us: 1.32x faster                                                 |
| go                         | 141 ms                                                 | 111 ms: 1.27x faster                                                  |
| async_tree_none_tg         | 319 ms                                                 | 252 ms: 1.27x faster                                                  |
| deepcopy_reduce            | 3.24 us                                                | 2.71 us: 1.19x faster                                                 |
| regex_effbot               | 3.77 ms                                                | 3.25 ms: 1.16x faster                                                 |
| regex_v8                   | 26.9 ms                                                | 23.3 ms: 1.15x faster                                                 |
| async_tree_cpu_io_mixed    | 573 ms                                                 | 508 ms: 1.13x faster                                                  |
| pylint                     | 312 ms                                                 | 279 ms: 1.12x faster                                                  |
| richards                   | 47.5 ms                                                | 43.0 ms: 1.10x faster                                                 |
| pyflate                    | 470 ms                                                 | 427 ms: 1.10x faster                                                  |
| float                      | 78.7 ms                                                | 71.5 ms: 1.10x faster                                                 |
| richards_super             | 53.7 ms                                                | 49.2 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 499 ms: 1.09x faster                                                  |
| dulwich_log                | 64.6 ms                                                | 60.1 ms: 1.08x faster                                                 |
| xml_etree_parse            | 154 ms                                                 | 144 ms: 1.07x faster                                                  |
| async_generators           | 433 ms                                                 | 409 ms: 1.06x faster                                                  |
| regex_dna                  | 220 ms                                                 | 210 ms: 1.05x faster                                                  |
| sympy_integrate            | 19.8 ms                                                | 19.0 ms: 1.04x faster                                                 |
| python_startup             | 12.7 ms                                                | 12.2 ms: 1.04x faster                                                 |
| k_core                     | 2.37 sec                                               | 2.28 sec: 1.04x faster                                                |
| genshi_text                | 22.6 ms                                                | 21.8 ms: 1.04x faster                                                 |
| 2to3                       | 266 ms                                                 | 256 ms: 1.04x faster                                                  |
| spectral_norm              | 113 ms                                                 | 109 ms: 1.04x faster                                                  |
| regex_compile              | 132 ms                                                 | 127 ms: 1.04x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.03x faster                                                |
| gc_traversal               | 4.90 ms                                                | 4.75 ms: 1.03x faster                                                 |
| telco                      | 8.40 ms                                                | 8.15 ms: 1.03x faster                                                 |
| tomli_loads                | 2.12 sec                                               | 2.06 sec: 1.03x faster                                                |
| bpe_tokeniser              | 4.69 sec                                               | 4.57 sec: 1.03x faster                                                |
| html5lib                   | 63.4 ms                                                | 62.0 ms: 1.02x faster                                                 |
| meteor_contest             | 108 ms                                                 | 106 ms: 1.02x faster                                                  |
| sphinx                     | 1.03 sec                                               | 1.02 sec: 1.02x faster                                                |
| sympy_str                  | 273 ms                                                 | 269 ms: 1.02x faster                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 99.7 ms: 1.02x faster                                                 |
| python_startup_no_site     | 7.00 ms                                                | 6.90 ms: 1.01x faster                                                 |
| sqlite_synth               | 2.90 us                                                | 2.86 us: 1.01x faster                                                 |
| comprehensions             | 16.5 us                                                | 16.3 us: 1.01x faster                                                 |
| genshi_xml                 | 50.5 ms                                                | 49.9 ms: 1.01x faster                                                 |
| xml_etree_generate         | 86.8 ms                                                | 85.9 ms: 1.01x faster                                                 |
| sympy_sum                  | 150 ms                                                 | 149 ms: 1.01x faster                                                  |
| scimark_sor                | 122 ms                                                 | 121 ms: 1.01x faster                                                  |
| hexiom                     | 6.08 ms                                                | 6.05 ms: 1.00x faster                                                 |
| scimark_monte_carlo        | 66.8 ms                                                | 67.2 ms: 1.01x slower                                                 |
| crypto_pyaes               | 74.7 ms                                                | 75.2 ms: 1.01x slower                                                 |
| pathlib                    | 17.4 ms                                                | 17.5 ms: 1.01x slower                                                 |
| xml_etree_process          | 60.5 ms                                                | 61.0 ms: 1.01x slower                                                 |
| nqueens                    | 80.9 ms                                                | 81.7 ms: 1.01x slower                                                 |
| django_template            | 31.7 ms                                                | 32.3 ms: 1.02x slower                                                 |
| unpickle_pure_python       | 213 us                                                 | 219 us: 1.03x slower                                                  |
| pidigits                   | 186 ms                                                 | 192 ms: 1.03x slower                                                  |
| raytrace                   | 262 ms                                                 | 270 ms: 1.03x slower                                                  |
| scimark_fft                | 367 ms                                                 | 379 ms: 1.03x slower                                                  |
| generators                 | 28.8 ms                                                | 29.8 ms: 1.03x slower                                                 |
| scimark_lu                 | 114 ms                                                 | 119 ms: 1.04x slower                                                  |
| typing_runtime_protocols   | 160 us                                                 | 167 us: 1.04x slower                                                  |
| create_gc_cycles           | 2.45 ms                                                | 2.56 ms: 1.04x slower                                                 |
| json_loads                 | 27.2 us                                                | 28.5 us: 1.05x slower                                                 |
| chaos                      | 58.0 ms                                                | 61.3 ms: 1.06x slower                                                 |
| connected_components       | 447 ms                                                 | 473 ms: 1.06x slower                                                  |
| mako                       | 10.7 ms                                                | 11.3 ms: 1.06x slower                                                 |
| pickle_pure_python         | 302 us                                                 | 321 us: 1.06x slower                                                  |
| shortest_path              | 487 ms                                                 | 518 ms: 1.06x slower                                                  |
| fannkuch                   | 394 ms                                                 | 421 ms: 1.07x slower                                                  |
| pprint_safe_repr           | 727 ms                                                 | 786 ms: 1.08x slower                                                  |
| pprint_pformat             | 1.48 sec                                               | 1.62 sec: 1.10x slower                                                |
| logging_simple             | 5.65 us                                                | 6.19 us: 1.10x slower                                                 |
| json_dumps                 | 10.1 ms                                                | 11.1 ms: 1.10x slower                                                 |
| deltablue                  | 3.19 ms                                                | 3.55 ms: 1.11x slower                                                 |
| logging_format             | 6.23 us                                                | 6.97 us: 1.12x slower                                                 |
| coroutines                 | 22.2 ms                                                | 25.0 ms: 1.12x slower                                                 |
| many_optionals             | 857 us                                                 | 967 us: 1.13x slower                                                  |
| nbody                      | 87.7 ms                                                | 102 ms: 1.16x slower                                                  |
| subparsers                 | 15.5 ms                                                | 23.7 ms: 1.53x slower                                                 |
| logging_silent             | 101 ns                                                 | 477 ns: 4.72x slower                                                  |
| coverage                   | 82.8 ms                                                | 439 ms: 5.30x slower                                                  |
| thrift                     | 800 us                                                 | 148 ms: 185.22x slower                                                |
| Geometric mean             | (ref)                                                  | 1.06x slower                                                          |

Benchmark hidden because not significant (5): scimark_sparse_mat_mult, json, docutils, sympy_expand, asyncio_websockets
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250608-3.15.0a0-aac22ea/bm-20250608-linux-x86_64-python-aac22ea212849f8fffee-3.15.0a0-aac22ea.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.042x slower

# HPT report

- Reliability score: 97.79% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x