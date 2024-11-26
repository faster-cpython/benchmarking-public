# Results vs. 3.13.0

- fork: python
- ref: c0f045f7fd3bb7ccf982
- machine: linux-x86_64
- commit hash: c0f045f
- commit date: 2024-11-15
- overall geometric mean: 1.005x faster
- HPT reliability: 79.16%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 256 ms: 1.04x faster                                                   |
| docutils       | 2.59 sec                                               | 2.70 sec: 1.04x slower                                                 |
| html5lib       | 64.2 ms                                                | 65.5 ms: 1.02x slower                                                  |
| sphinx         | 1.03 sec                                               | 1.06 sec: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 380 ms: 1.22x faster                                                   |
| async_tree_memoization     | 442 ms                                                 | 414 ms: 1.07x faster                                                   |
| async_tree_none            | 351 ms                                                 | 330 ms: 1.06x faster                                                   |
| async_generators           | 436 ms                                                 | 429 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 566 ms: 1.04x slower                                                   |
| coroutines                 | 22.7 ms                                                | 24.0 ms: 1.06x slower                                                  |
| async_tree_io_tg           | 857 ms                                                 | 976 ms: 1.14x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed, asyncio_websockets, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                   |
| float          | 79.2 ms                                                | 80.2 ms: 1.01x slower                                                  |
| nbody          | 87.0 ms                                                | 97.2 ms: 1.12x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.6 ms: 1.07x faster                                                  |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                   |
| regex_effbot   | 3.73 ms                                                | 3.83 ms: 1.03x slower                                                  |
| regex_dna      | 218 ms                                                 | 225 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_process    | 60.6 ms                                                | 59.2 ms: 1.02x faster                                                  |
| tomli_loads          | 2.14 sec                                               | 2.09 sec: 1.02x faster                                                 |
| json_loads           | 27.2 us                                                | 26.8 us: 1.01x faster                                                  |
| xml_etree_generate   | 86.7 ms                                                | 85.5 ms: 1.01x faster                                                  |
| unpickle_pure_python | 216 us                                                 | 219 us: 1.02x slower                                                   |
| xml_etree_parse      | 156 ms                                                 | 159 ms: 1.02x slower                                                   |
| xml_etree_iterparse  | 101 ms                                                 | 106 ms: 1.05x slower                                                   |
| pickle_pure_python   | 310 us                                                 | 329 us: 1.06x slower                                                   |
| json_dumps           | 10.6 ms                                                | 11.3 ms: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.02 ms: 1.01x slower                                                  |
| python_startup         | 12.5 ms                                                | 12.7 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 35.2 ms                                                | 32.1 ms: 1.10x faster                                                  |
| genshi_text     | 23.5 ms                                                | 22.3 ms: 1.05x faster                                                  |
| genshi_xml      | 50.9 ms                                                | 50.4 ms: 1.01x faster                                                  |
| mako            | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 259 us: 1.38x faster                                                   |
| deepcopy_memo              | 39.1 us                                                | 30.4 us: 1.29x faster                                                  |
| async_tree_memoization_tg  | 464 ms                                                 | 380 ms: 1.22x faster                                                   |
| deepcopy_reduce            | 3.20 us                                                | 2.70 us: 1.18x faster                                                  |
| go                         | 144 ms                                                 | 123 ms: 1.17x faster                                                   |
| pathlib                    | 17.5 ms                                                | 16.0 ms: 1.10x faster                                                  |
| django_template            | 35.2 ms                                                | 32.1 ms: 1.10x faster                                                  |
| telco                      | 8.54 ms                                                | 7.81 ms: 1.09x faster                                                  |
| json                       | 5.36 ms                                                | 4.99 ms: 1.08x faster                                                  |
| async_tree_memoization     | 442 ms                                                 | 414 ms: 1.07x faster                                                   |
| regex_v8                   | 26.2 ms                                                | 24.6 ms: 1.07x faster                                                  |
| async_tree_none            | 351 ms                                                 | 330 ms: 1.06x faster                                                   |
| genshi_text                | 23.5 ms                                                | 22.3 ms: 1.05x faster                                                  |
| pycparser                  | 1.20 sec                                               | 1.14 sec: 1.05x faster                                                 |
| richards                   | 48.7 ms                                                | 46.3 ms: 1.05x faster                                                  |
| 2to3                       | 267 ms                                                 | 256 ms: 1.04x faster                                                   |
| thrift                     | 809 us                                                 | 776 us: 1.04x faster                                                   |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                                   |
| logging_format             | 6.40 us                                                | 6.18 us: 1.04x faster                                                  |
| richards_super             | 54.9 ms                                                | 53.1 ms: 1.03x faster                                                  |
| logging_simple             | 5.72 us                                                | 5.55 us: 1.03x faster                                                  |
| xml_etree_process          | 60.6 ms                                                | 59.2 ms: 1.02x faster                                                  |
| tomli_loads                | 2.14 sec                                               | 2.09 sec: 1.02x faster                                                 |
| typing_runtime_protocols   | 165 us                                                 | 161 us: 1.02x faster                                                   |
| crypto_pyaes               | 75.3 ms                                                | 73.8 ms: 1.02x faster                                                  |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.02x faster                                                   |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                                   |
| sympy_str                  | 275 ms                                                 | 270 ms: 1.02x faster                                                   |
| regex_compile              | 132 ms                                                 | 130 ms: 1.02x faster                                                   |
| async_generators           | 436 ms                                                 | 429 ms: 1.02x faster                                                   |
| json_loads                 | 27.2 us                                                | 26.8 us: 1.01x faster                                                  |
| sympy_expand               | 463 ms                                                 | 457 ms: 1.01x faster                                                   |
| mdp                        | 2.72 sec                                               | 2.68 sec: 1.01x faster                                                 |
| xml_etree_generate         | 86.7 ms                                                | 85.5 ms: 1.01x faster                                                  |
| connected_components       | 444 ms                                                 | 438 ms: 1.01x faster                                                   |
| genshi_xml                 | 50.9 ms                                                | 50.4 ms: 1.01x faster                                                  |
| pyflate                    | 471 ms                                                 | 467 ms: 1.01x faster                                                   |
| pprint_pformat             | 1.49 sec                                               | 1.48 sec: 1.01x faster                                                 |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 5.00 ms: 1.01x faster                                                  |
| sqlglot_optimize           | 53.7 ms                                                | 53.4 ms: 1.01x faster                                                  |
| generators                 | 29.0 ms                                                | 28.8 ms: 1.01x faster                                                  |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                                   |
| spectral_norm              | 115 ms                                                 | 115 ms: 1.01x faster                                                   |
| scimark_fft                | 364 ms                                                 | 363 ms: 1.00x faster                                                   |
| sympy_integrate            | 19.9 ms                                                | 20.0 ms: 1.00x slower                                                  |
| coverage                   | 84.0 ms                                                | 84.6 ms: 1.01x slower                                                  |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                   |
| bpe_tokeniser              | 4.75 sec                                               | 4.78 sec: 1.01x slower                                                 |
| python_startup_no_site     | 6.96 ms                                                | 7.02 ms: 1.01x slower                                                  |
| sqlglot_transpile          | 1.58 ms                                                | 1.60 ms: 1.01x slower                                                  |
| float                      | 79.2 ms                                                | 80.2 ms: 1.01x slower                                                  |
| fannkuch                   | 404 ms                                                 | 410 ms: 1.01x slower                                                   |
| unpickle_pure_python       | 216 us                                                 | 219 us: 1.02x slower                                                   |
| python_startup             | 12.5 ms                                                | 12.7 ms: 1.02x slower                                                  |
| nqueens                    | 78.4 ms                                                | 79.8 ms: 1.02x slower                                                  |
| xml_etree_parse            | 156 ms                                                 | 159 ms: 1.02x slower                                                   |
| html5lib                   | 64.2 ms                                                | 65.5 ms: 1.02x slower                                                  |
| sphinx                     | 1.03 sec                                               | 1.06 sec: 1.02x slower                                                 |
| dulwich_log                | 64.3 ms                                                | 65.8 ms: 1.02x slower                                                  |
| sqlglot_parse              | 1.27 ms                                                | 1.30 ms: 1.02x slower                                                  |
| regex_effbot               | 3.73 ms                                                | 3.83 ms: 1.03x slower                                                  |
| scimark_monte_carlo        | 67.4 ms                                                | 69.3 ms: 1.03x slower                                                  |
| regex_dna                  | 218 ms                                                 | 225 ms: 1.03x slower                                                   |
| raytrace                   | 267 ms                                                 | 275 ms: 1.03x slower                                                   |
| logging_silent             | 102 ns                                                 | 105 ns: 1.03x slower                                                   |
| mako                       | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                  |
| hexiom                     | 6.16 ms                                                | 6.35 ms: 1.03x slower                                                  |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 566 ms: 1.04x slower                                                   |
| bench_thread_pool          | 822 us                                                 | 853 us: 1.04x slower                                                   |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                                  |
| docutils                   | 2.59 sec                                               | 2.70 sec: 1.04x slower                                                 |
| scimark_lu                 | 113 ms                                                 | 117 ms: 1.04x slower                                                   |
| scimark_sor                | 124 ms                                                 | 129 ms: 1.05x slower                                                   |
| deltablue                  | 3.23 ms                                                | 3.37 ms: 1.05x slower                                                  |
| xml_etree_iterparse        | 101 ms                                                 | 106 ms: 1.05x slower                                                   |
| gc_traversal               | 4.37 ms                                                | 4.61 ms: 1.05x slower                                                  |
| chaos                      | 58.1 ms                                                | 61.4 ms: 1.06x slower                                                  |
| coroutines                 | 22.7 ms                                                | 24.0 ms: 1.06x slower                                                  |
| pickle_pure_python         | 310 us                                                 | 329 us: 1.06x slower                                                   |
| json_dumps                 | 10.6 ms                                                | 11.3 ms: 1.07x slower                                                  |
| nbody                      | 87.0 ms                                                | 97.2 ms: 1.12x slower                                                  |
| create_gc_cycles           | 2.41 ms                                                | 2.70 ms: 1.12x slower                                                  |
| async_tree_io_tg           | 857 ms                                                 | 976 ms: 1.14x slower                                                   |
| k_core                     | 2.35 sec                                               | 3.61 sec: 1.53x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 78.4 ms: 3.27x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, shortest_path, sqlalchemy_imperative, pprint_safe_repr, asyncio_websockets, async_tree_none_tg, async_tree_io, pylint
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241115-3.14.0a1+-c0f045f/bm-20241115-linux-x86_64-python-c0f045f7fd3bb7ccf982-3.14.0a1+-c0f045f.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.005x faster
# HPT report

- Reliability score: 79.16% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x