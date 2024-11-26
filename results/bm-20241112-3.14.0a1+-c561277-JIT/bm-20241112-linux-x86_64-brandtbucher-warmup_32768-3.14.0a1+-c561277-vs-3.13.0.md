# Results vs. 3.13.0

- fork: brandtbucher
- ref: warmup_32768
- machine: linux-x86_64
- commit hash: c561277
- commit date: 2024-11-12
- overall geometric mean: 1.006x faster
- HPT reliability: 66.10%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 256 ms: 1.04x faster                                                 |
| docutils       | 2.59 sec                                               | 2.83 sec: 1.09x slower                                               |
| html5lib       | 64.2 ms                                                | 66.5 ms: 1.04x slower                                                |
| sphinx         | 1.03 sec                                               | 1.10 sec: 1.06x slower                                               |
| Geometric mean | (ref)                                                  | 1.04x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 380 ms: 1.22x faster                                                 |
| async_tree_memoization     | 442 ms                                                 | 419 ms: 1.06x faster                                                 |
| async_tree_none            | 351 ms                                                 | 335 ms: 1.05x faster                                                 |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.01x slower                                                |
| async_tree_io              | 842 ms                                                 | 866 ms: 1.03x slower                                                 |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 565 ms: 1.03x slower                                                 |
| async_generators           | 436 ms                                                 | 461 ms: 1.06x slower                                                 |
| async_tree_io_tg           | 857 ms                                                 | 986 ms: 1.15x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (3): asyncio_websockets, async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 76.5 ms: 1.04x faster                                                |
| nbody          | 87.0 ms                                                | 84.5 ms: 1.03x faster                                                |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.1 ms: 1.05x faster                                                |
| regex_effbot   | 3.73 ms                                                | 3.58 ms: 1.04x faster                                                |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                 |
| regex_dna      | 218 ms                                                 | 215 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 78.1 ms: 1.11x faster                                                |
| tomli_loads          | 2.14 sec                                               | 1.96 sec: 1.09x faster                                               |
| xml_etree_process    | 60.6 ms                                                | 55.6 ms: 1.09x faster                                                |
| unpickle_pure_python | 216 us                                                 | 199 us: 1.08x faster                                                 |
| json_loads           | 27.2 us                                                | 26.7 us: 1.02x faster                                                |
| xml_etree_iterparse  | 101 ms                                                 | 102 ms: 1.01x slower                                                 |
| json_dumps           | 10.6 ms                                                | 11.0 ms: 1.05x slower                                                |
| pickle_pure_python   | 310 us                                                 | 326 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                         |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                |
| python_startup         | 12.5 ms                                                | 12.7 ms: 1.02x slower                                                |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.2 ms: 1.08x faster                                                |
| genshi_text     | 23.5 ms                                                | 23.7 ms: 1.01x slower                                                |
| django_template | 35.2 ms                                                | 36.3 ms: 1.03x slower                                                |
| genshi_xml      | 50.9 ms                                                | 56.9 ms: 1.12x slower                                                |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 270 us: 1.33x faster                                                 |
| deepcopy_memo              | 39.1 us                                                | 29.9 us: 1.31x faster                                                |
| async_tree_memoization_tg  | 464 ms                                                 | 380 ms: 1.22x faster                                                 |
| deepcopy_reduce            | 3.20 us                                                | 2.72 us: 1.17x faster                                                |
| scimark_fft                | 364 ms                                                 | 319 ms: 1.14x faster                                                 |
| go                         | 144 ms                                                 | 129 ms: 1.12x faster                                                 |
| telco                      | 8.54 ms                                                | 7.69 ms: 1.11x faster                                                |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.54 ms: 1.11x faster                                                |
| xml_etree_generate         | 86.7 ms                                                | 78.1 ms: 1.11x faster                                                |
| crypto_pyaes               | 75.3 ms                                                | 68.0 ms: 1.11x faster                                                |
| json                       | 5.36 ms                                                | 4.88 ms: 1.10x faster                                                |
| tomli_loads                | 2.14 sec                                               | 1.96 sec: 1.09x faster                                               |
| xml_etree_process          | 60.6 ms                                                | 55.6 ms: 1.09x faster                                                |
| mako                       | 11.1 ms                                                | 10.2 ms: 1.08x faster                                                |
| unpickle_pure_python       | 216 us                                                 | 199 us: 1.08x faster                                                 |
| pathlib                    | 17.5 ms                                                | 16.2 ms: 1.08x faster                                                |
| richards                   | 48.7 ms                                                | 45.5 ms: 1.07x faster                                                |
| bpe_tokeniser              | 4.75 sec                                               | 4.47 sec: 1.06x faster                                               |
| async_tree_memoization     | 442 ms                                                 | 419 ms: 1.06x faster                                                 |
| richards_super             | 54.9 ms                                                | 52.2 ms: 1.05x faster                                                |
| async_tree_none            | 351 ms                                                 | 335 ms: 1.05x faster                                                 |
| regex_v8                   | 26.2 ms                                                | 25.1 ms: 1.05x faster                                                |
| regex_effbot               | 3.73 ms                                                | 3.58 ms: 1.04x faster                                                |
| 2to3                       | 267 ms                                                 | 256 ms: 1.04x faster                                                 |
| thrift                     | 809 us                                                 | 780 us: 1.04x faster                                                 |
| float                      | 79.2 ms                                                | 76.5 ms: 1.04x faster                                                |
| sqlalchemy_declarative     | 133 ms                                                 | 129 ms: 1.03x faster                                                 |
| scimark_monte_carlo        | 67.4 ms                                                | 65.4 ms: 1.03x faster                                                |
| nbody                      | 87.0 ms                                                | 84.5 ms: 1.03x faster                                                |
| fannkuch                   | 404 ms                                                 | 394 ms: 1.03x faster                                                 |
| logging_format             | 6.40 us                                                | 6.25 us: 1.02x faster                                                |
| scimark_sor                | 124 ms                                                 | 121 ms: 1.02x faster                                                 |
| regex_compile              | 132 ms                                                 | 130 ms: 1.02x faster                                                 |
| json_loads                 | 27.2 us                                                | 26.7 us: 1.02x faster                                                |
| deltablue                  | 3.23 ms                                                | 3.17 ms: 1.02x faster                                                |
| connected_components       | 444 ms                                                 | 436 ms: 1.02x faster                                                 |
| regex_dna                  | 218 ms                                                 | 215 ms: 1.01x faster                                                 |
| pycparser                  | 1.20 sec                                               | 1.19 sec: 1.01x faster                                               |
| meteor_contest             | 109 ms                                                 | 109 ms: 1.00x slower                                                 |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                 |
| mdp                        | 2.72 sec                                               | 2.73 sec: 1.01x slower                                               |
| sqlglot_transpile          | 1.58 ms                                                | 1.59 ms: 1.01x slower                                                |
| genshi_text                | 23.5 ms                                                | 23.7 ms: 1.01x slower                                                |
| xml_etree_iterparse        | 101 ms                                                 | 102 ms: 1.01x slower                                                 |
| sqlglot_optimize           | 53.7 ms                                                | 54.3 ms: 1.01x slower                                                |
| sympy_str                  | 275 ms                                                 | 278 ms: 1.01x slower                                                 |
| sqlglot_normalize          | 108 ms                                                 | 109 ms: 1.01x slower                                                 |
| python_startup_no_site     | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.01x slower                                                |
| scimark_lu                 | 113 ms                                                 | 114 ms: 1.01x slower                                                 |
| python_startup             | 12.5 ms                                                | 12.7 ms: 1.02x slower                                                |
| coverage                   | 84.0 ms                                                | 85.3 ms: 1.02x slower                                                |
| typing_runtime_protocols   | 165 us                                                 | 167 us: 1.02x slower                                                 |
| sympy_integrate            | 19.9 ms                                                | 20.3 ms: 1.02x slower                                                |
| spectral_norm              | 115 ms                                                 | 118 ms: 1.03x slower                                                 |
| pprint_safe_repr           | 728 ms                                                 | 749 ms: 1.03x slower                                                 |
| async_tree_io              | 842 ms                                                 | 866 ms: 1.03x slower                                                 |
| sympy_sum                  | 150 ms                                                 | 155 ms: 1.03x slower                                                 |
| chaos                      | 58.1 ms                                                | 59.9 ms: 1.03x slower                                                |
| pprint_pformat             | 1.49 sec                                               | 1.54 sec: 1.03x slower                                               |
| django_template            | 35.2 ms                                                | 36.3 ms: 1.03x slower                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 565 ms: 1.03x slower                                                 |
| gc_traversal               | 4.37 ms                                                | 4.52 ms: 1.03x slower                                                |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.04x slower                                                |
| html5lib                   | 64.2 ms                                                | 66.5 ms: 1.04x slower                                                |
| raytrace                   | 267 ms                                                 | 278 ms: 1.04x slower                                                 |
| sympy_expand               | 463 ms                                                 | 483 ms: 1.04x slower                                                 |
| json_dumps                 | 10.6 ms                                                | 11.0 ms: 1.05x slower                                                |
| pickle_pure_python         | 310 us                                                 | 326 us: 1.05x slower                                                 |
| async_generators           | 436 ms                                                 | 461 ms: 1.06x slower                                                 |
| comprehensions             | 16.5 us                                                | 17.4 us: 1.06x slower                                                |
| bench_thread_pool          | 822 us                                                 | 873 us: 1.06x slower                                                 |
| sphinx                     | 1.03 sec                                               | 1.10 sec: 1.06x slower                                               |
| hexiom                     | 6.16 ms                                                | 6.68 ms: 1.08x slower                                                |
| docutils                   | 2.59 sec                                               | 2.83 sec: 1.09x slower                                               |
| create_gc_cycles           | 2.41 ms                                                | 2.67 ms: 1.11x slower                                                |
| genshi_xml                 | 50.9 ms                                                | 56.9 ms: 1.12x slower                                                |
| async_tree_io_tg           | 857 ms                                                 | 986 ms: 1.15x slower                                                 |
| nqueens                    | 78.4 ms                                                | 90.6 ms: 1.16x slower                                                |
| generators                 | 29.0 ms                                                | 36.0 ms: 1.24x slower                                                |
| k_core                     | 2.35 sec                                               | 3.65 sec: 1.55x slower                                               |
| bench_mp_pool              | 24.0 ms                                                | 78.4 ms: 3.27x slower                                                |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (11): sqlalchemy_imperative, logging_silent, xml_etree_parse, shortest_path, logging_simple, dulwich_log, asyncio_websockets, pyflate, async_tree_cpu_io_mixed, async_tree_none_tg, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (1) of results/bm-20241112-3.14.0a1+-c561277-JIT/bm-20241112-linux-x86_64-brandtbucher-warmup_32768-3.14.0a1+-c561277.json: sqlite_synth

- Geometric mean (including insignificant results): 1.006x faster
# HPT report

- Reliability score: 66.10% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.03x