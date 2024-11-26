# Results vs. 3.13.0

- fork: brandtbucher
- ref: optimize_off_all
- machine: linux-x86_64
- commit hash: dff2fa8
- commit date: 2024-11-17
- overall geometric mean: 1.071x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 303 ms: 1.14x slower                                                     |
| docutils       | 2.59 sec                                               | 3.27 sec: 1.26x slower                                                   |
| html5lib       | 64.2 ms                                                | 68.5 ms: 1.07x slower                                                    |
| sphinx         | 1.03 sec                                               | 1.21 sec: 1.17x slower                                                   |
| Geometric mean | (ref)                                                  | 1.16x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 389 ms: 1.19x faster                                                     |
| async_tree_none            | 351 ms                                                 | 343 ms: 1.02x faster                                                     |
| coroutines                 | 22.7 ms                                                | 22.4 ms: 1.01x faster                                                    |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.00x slower                                                     |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 592 ms: 1.03x slower                                                     |
| async_tree_none_tg         | 321 ms                                                 | 330 ms: 1.03x slower                                                     |
| async_tree_io              | 842 ms                                                 | 882 ms: 1.05x slower                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 574 ms: 1.05x slower                                                     |
| async_generators           | 436 ms                                                 | 462 ms: 1.06x slower                                                     |
| async_tree_io_tg           | 857 ms                                                 | 987 ms: 1.15x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                     |
| float          | 79.2 ms                                                | 81.7 ms: 1.03x slower                                                    |
| nbody          | 87.0 ms                                                | 102 ms: 1.17x slower                                                     |
| Geometric mean | (ref)                                                  | 1.07x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.1 ms: 1.05x faster                                                    |
| regex_effbot   | 3.73 ms                                                | 3.62 ms: 1.03x faster                                                    |
| regex_compile  | 132 ms                                                 | 162 ms: 1.22x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x slower                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_loads           | 27.2 us                                                | 26.2 us: 1.04x faster                                                    |
| xml_etree_parse      | 156 ms                                                 | 150 ms: 1.04x faster                                                     |
| tomli_loads          | 2.14 sec                                               | 2.08 sec: 1.03x faster                                                   |
| xml_etree_generate   | 86.7 ms                                                | 86.3 ms: 1.01x faster                                                    |
| xml_etree_iterparse  | 101 ms                                                 | 104 ms: 1.02x slower                                                     |
| xml_etree_process    | 60.6 ms                                                | 62.2 ms: 1.03x slower                                                    |
| unpickle_pure_python | 216 us                                                 | 229 us: 1.06x slower                                                     |
| json_dumps           | 10.6 ms                                                | 11.4 ms: 1.08x slower                                                    |
| pickle_pure_python   | 310 us                                                 | 350 us: 1.13x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.08 ms: 1.02x slower                                                    |
| python_startup         | 12.5 ms                                                | 12.8 ms: 1.02x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 11.0 ms: 1.01x faster                                                    |
| django_template | 35.2 ms                                                | 35.8 ms: 1.02x slower                                                    |
| genshi_text     | 23.5 ms                                                | 27.3 ms: 1.16x slower                                                    |
| genshi_xml      | 50.9 ms                                                | 67.0 ms: 1.32x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.11x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 389 ms: 1.19x faster                                                     |
| deepcopy                   | 358 us                                                 | 303 us: 1.18x faster                                                     |
| deepcopy_memo              | 39.1 us                                                | 34.5 us: 1.13x faster                                                    |
| telco                      | 8.54 ms                                                | 7.83 ms: 1.09x faster                                                    |
| json                       | 5.36 ms                                                | 4.95 ms: 1.08x faster                                                    |
| pathlib                    | 17.5 ms                                                | 16.4 ms: 1.07x faster                                                    |
| deepcopy_reduce            | 3.20 us                                                | 3.01 us: 1.06x faster                                                    |
| scimark_fft                | 364 ms                                                 | 347 ms: 1.05x faster                                                     |
| regex_v8                   | 26.2 ms                                                | 25.1 ms: 1.05x faster                                                    |
| json_loads                 | 27.2 us                                                | 26.2 us: 1.04x faster                                                    |
| xml_etree_parse            | 156 ms                                                 | 150 ms: 1.04x faster                                                     |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.88 ms: 1.03x faster                                                    |
| mdp                        | 2.72 sec                                               | 2.64 sec: 1.03x faster                                                   |
| regex_effbot               | 3.73 ms                                                | 3.62 ms: 1.03x faster                                                    |
| tomli_loads                | 2.14 sec                                               | 2.08 sec: 1.03x faster                                                   |
| crypto_pyaes               | 75.3 ms                                                | 73.5 ms: 1.02x faster                                                    |
| async_tree_none            | 351 ms                                                 | 343 ms: 1.02x faster                                                     |
| thrift                     | 809 us                                                 | 794 us: 1.02x faster                                                     |
| coroutines                 | 22.7 ms                                                | 22.4 ms: 1.01x faster                                                    |
| mako                       | 11.1 ms                                                | 11.0 ms: 1.01x faster                                                    |
| logging_format             | 6.40 us                                                | 6.34 us: 1.01x faster                                                    |
| xml_etree_generate         | 86.7 ms                                                | 86.3 ms: 1.01x faster                                                    |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x slower                                                     |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.00x slower                                                     |
| connected_components       | 444 ms                                                 | 448 ms: 1.01x slower                                                     |
| bpe_tokeniser              | 4.75 sec                                               | 4.80 sec: 1.01x slower                                                   |
| logging_simple             | 5.72 us                                                | 5.81 us: 1.02x slower                                                    |
| python_startup_no_site     | 6.96 ms                                                | 7.08 ms: 1.02x slower                                                    |
| django_template            | 35.2 ms                                                | 35.8 ms: 1.02x slower                                                    |
| shortest_path              | 481 ms                                                 | 491 ms: 1.02x slower                                                     |
| xml_etree_iterparse        | 101 ms                                                 | 104 ms: 1.02x slower                                                     |
| python_startup             | 12.5 ms                                                | 12.8 ms: 1.02x slower                                                    |
| xml_etree_process          | 60.6 ms                                                | 62.2 ms: 1.03x slower                                                    |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 592 ms: 1.03x slower                                                     |
| async_tree_none_tg         | 321 ms                                                 | 330 ms: 1.03x slower                                                     |
| meteor_contest             | 109 ms                                                 | 112 ms: 1.03x slower                                                     |
| richards                   | 48.7 ms                                                | 50.2 ms: 1.03x slower                                                    |
| float                      | 79.2 ms                                                | 81.7 ms: 1.03x slower                                                    |
| gc_traversal               | 4.37 ms                                                | 4.53 ms: 1.04x slower                                                    |
| async_tree_io              | 842 ms                                                 | 882 ms: 1.05x slower                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 574 ms: 1.05x slower                                                     |
| go                         | 144 ms                                                 | 152 ms: 1.06x slower                                                     |
| sqlalchemy_imperative      | 17.1 ms                                                | 18.1 ms: 1.06x slower                                                    |
| async_generators           | 436 ms                                                 | 462 ms: 1.06x slower                                                     |
| unpickle_pure_python       | 216 us                                                 | 229 us: 1.06x slower                                                     |
| fannkuch                   | 404 ms                                                 | 430 ms: 1.06x slower                                                     |
| pycparser                  | 1.20 sec                                               | 1.28 sec: 1.07x slower                                                   |
| html5lib                   | 64.2 ms                                                | 68.5 ms: 1.07x slower                                                    |
| richards_super             | 54.9 ms                                                | 58.7 ms: 1.07x slower                                                    |
| pyflate                    | 471 ms                                                 | 507 ms: 1.08x slower                                                     |
| json_dumps                 | 10.6 ms                                                | 11.4 ms: 1.08x slower                                                    |
| typing_runtime_protocols   | 165 us                                                 | 179 us: 1.09x slower                                                     |
| scimark_monte_carlo        | 67.4 ms                                                | 73.6 ms: 1.09x slower                                                    |
| dulwich_log                | 64.3 ms                                                | 71.1 ms: 1.10x slower                                                    |
| spectral_norm              | 115 ms                                                 | 128 ms: 1.11x slower                                                     |
| scimark_sor                | 124 ms                                                 | 138 ms: 1.11x slower                                                     |
| create_gc_cycles           | 2.41 ms                                                | 2.68 ms: 1.11x slower                                                    |
| bench_thread_pool          | 822 us                                                 | 916 us: 1.11x slower                                                     |
| deltablue                  | 3.23 ms                                                | 3.63 ms: 1.13x slower                                                    |
| pickle_pure_python         | 310 us                                                 | 350 us: 1.13x slower                                                     |
| scimark_lu                 | 113 ms                                                 | 128 ms: 1.13x slower                                                     |
| 2to3                       | 267 ms                                                 | 303 ms: 1.14x slower                                                     |
| logging_silent             | 102 ns                                                 | 116 ns: 1.14x slower                                                     |
| sqlglot_parse              | 1.27 ms                                                | 1.46 ms: 1.15x slower                                                    |
| sqlalchemy_declarative     | 133 ms                                                 | 153 ms: 1.15x slower                                                     |
| raytrace                   | 267 ms                                                 | 307 ms: 1.15x slower                                                     |
| async_tree_io_tg           | 857 ms                                                 | 987 ms: 1.15x slower                                                     |
| sympy_expand               | 463 ms                                                 | 535 ms: 1.15x slower                                                     |
| genshi_text                | 23.5 ms                                                | 27.3 ms: 1.16x slower                                                    |
| chaos                      | 58.1 ms                                                | 67.6 ms: 1.16x slower                                                    |
| sqlglot_normalize          | 108 ms                                                 | 126 ms: 1.17x slower                                                     |
| sphinx                     | 1.03 sec                                               | 1.21 sec: 1.17x slower                                                   |
| nbody                      | 87.0 ms                                                | 102 ms: 1.17x slower                                                     |
| sympy_str                  | 275 ms                                                 | 325 ms: 1.18x slower                                                     |
| sqlglot_transpile          | 1.58 ms                                                | 1.88 ms: 1.19x slower                                                    |
| comprehensions             | 16.5 us                                                | 19.8 us: 1.20x slower                                                    |
| nqueens                    | 78.4 ms                                                | 95.0 ms: 1.21x slower                                                    |
| regex_compile              | 132 ms                                                 | 162 ms: 1.22x slower                                                     |
| sqlglot_optimize           | 53.7 ms                                                | 66.6 ms: 1.24x slower                                                    |
| sympy_sum                  | 150 ms                                                 | 187 ms: 1.24x slower                                                     |
| docutils                   | 2.59 sec                                               | 3.27 sec: 1.26x slower                                                   |
| pylint                     | 313 ms                                                 | 396 ms: 1.27x slower                                                     |
| sympy_integrate            | 19.9 ms                                                | 25.3 ms: 1.27x slower                                                    |
| genshi_xml                 | 50.9 ms                                                | 67.0 ms: 1.32x slower                                                    |
| pprint_safe_repr           | 728 ms                                                 | 995 ms: 1.37x slower                                                     |
| hexiom                     | 6.16 ms                                                | 8.50 ms: 1.38x slower                                                    |
| generators                 | 29.0 ms                                                | 40.9 ms: 1.41x slower                                                    |
| pprint_pformat             | 1.49 sec                                               | 2.14 sec: 1.43x slower                                                   |
| k_core                     | 2.35 sec                                               | 3.66 sec: 1.56x slower                                                   |
| bench_mp_pool              | 24.0 ms                                                | 85.8 ms: 3.58x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.09x slower                                                             |

Benchmark hidden because not significant (3): async_tree_memoization, regex_dna, coverage
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (4) of results/bm-20241117-3.14.0a1+-dff2fa8-JIT/bm-20241117-linux-x86_64-brandtbucher-optimize_off_all-3.14.0a1+-dff2fa8.json: djangocms, many_optionals, sqlite_synth, subparsers

- Geometric mean (including insignificant results): 1.071x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.10x