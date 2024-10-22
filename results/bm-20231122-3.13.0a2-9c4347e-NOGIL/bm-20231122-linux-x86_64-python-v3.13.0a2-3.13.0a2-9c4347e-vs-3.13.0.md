# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a2
- machine: linux-x86_64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.27x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x slower
- Memory change: 0.58x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 294 ms: 1.11x slower                                       |
| chameleon      | 6.85 ms                                                | 7.76 ms: 1.13x slower                                      |
| docutils       | 2.58 sec                                               | 2.89 sec: 1.12x slower                                     |
| html5lib       | 64.5 ms                                                | 71.7 ms: 1.11x slower                                      |
| tornado_http   | 91.5 ms                                                | 108 ms: 1.18x slower                                       |
| Geometric mean | (ref)                                                  | 1.13x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| asyncio_websockets         | 555 ms                                                 | 564 ms: 1.02x slower                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.03x slower                                     |
| asyncio_tcp                | 488 ms                                                 | 511 ms: 1.05x slower                                       |
| coroutines                 | 22.5 ms                                                | 24.8 ms: 1.10x slower                                      |
| async_generators           | 433 ms                                                 | 500 ms: 1.15x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 804 ms: 1.40x slower                                       |
| async_tree_none            | 354 ms                                                 | 509 ms: 1.44x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 657 ms: 1.48x slower                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 692 ms: 1.49x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 850 ms: 1.56x slower                                       |
| async_tree_io              | 843 ms                                                 | 1.39 sec: 1.65x slower                                     |
| async_tree_none_tg         | 320 ms                                                 | 540 ms: 1.69x slower                                       |
| async_tree_io_tg           | 825 ms                                                 | 1.45 sec: 1.76x slower                                     |
| Geometric mean             | (ref)                                                  | 1.35x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 194 ms: 1.04x slower                                       |
| float          | 78.5 ms                                                | 95.5 ms: 1.22x slower                                      |
| nbody          | 85.7 ms                                                | 110 ms: 1.28x slower                                       |
| Geometric mean | (ref)                                                  | 1.17x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.83 ms: 1.01x faster                                      |
| regex_dna      | 220 ms                                                 | 222 ms: 1.01x slower                                       |
| regex_v8       | 25.3 ms                                                | 25.9 ms: 1.02x slower                                      |
| regex_compile  | 131 ms                                                 | 149 ms: 1.14x slower                                       |
| Geometric mean | (ref)                                                  | 1.04x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_list          | 5.01 us                                                | 4.71 us: 1.06x faster                                      |
| pickle               | 11.6 us                                                | 11.4 us: 1.02x faster                                      |
| pickle_dict          | 33.2 us                                                | 32.7 us: 1.01x faster                                      |
| unpickle             | 14.9 us                                                | 15.4 us: 1.03x slower                                      |
| unpickle_list        | 4.96 us                                                | 5.26 us: 1.06x slower                                      |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.08x slower                                      |
| pickle_pure_python   | 300 us                                                 | 335 us: 1.12x slower                                       |
| tomli_loads          | 2.11 sec                                               | 2.37 sec: 1.12x slower                                     |
| xml_etree_iterparse  | 102 ms                                                 | 114 ms: 1.12x slower                                       |
| json_loads           | 27.0 us                                                | 30.9 us: 1.15x slower                                      |
| unpickle_pure_python | 213 us                                                 | 246 us: 1.15x slower                                       |
| xml_etree_parse      | 156 ms                                                 | 472 ms: 3.03x slower                                       |
| xml_etree_process    | 60.4 ms                                                | 1.03 sec: 17.03x slower                                    |
| xml_etree_generate   | 87.0 ms                                                | 1.58 sec: 18.18x slower                                    |
| Geometric mean       | (ref)                                                  | 1.71x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 11.1 ms: 1.05x slower                                      |
| python_startup_no_site | 6.99 ms                                                | 9.60 ms: 1.37x slower                                      |
| Geometric mean         | (ref)                                                  | 1.20x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 22.9 ms                                                | 24.9 ms: 1.09x slower                                      |
| django_template | 34.4 ms                                                | 38.3 ms: 1.11x slower                                      |
| genshi_xml      | 50.3 ms                                                | 56.2 ms: 1.12x slower                                      |
| mako            | 11.1 ms                                                | 12.9 ms: 1.17x slower                                      |
| Geometric mean  | (ref)                                                  | 1.12x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231122-linux-x86_64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 1.61 ms                                                | 1.22 ms: 1.32x faster                                      |
| typing_runtime_protocols   | 159 us                                                 | 127 us: 1.25x faster                                       |
| pickle_list                | 5.01 us                                                | 4.71 us: 1.06x faster                                      |
| bench_mp_pool              | 24.0 ms                                                | 22.6 ms: 1.06x faster                                      |
| gc_traversal               | 3.81 ms                                                | 3.64 ms: 1.04x faster                                      |
| pickle                     | 11.6 us                                                | 11.4 us: 1.02x faster                                      |
| regex_effbot               | 3.88 ms                                                | 3.83 ms: 1.01x faster                                      |
| pickle_dict                | 33.2 us                                                | 32.7 us: 1.01x faster                                      |
| regex_dna                  | 220 ms                                                 | 222 ms: 1.01x slower                                       |
| asyncio_websockets         | 555 ms                                                 | 564 ms: 1.02x slower                                       |
| regex_v8                   | 25.3 ms                                                | 25.9 ms: 1.02x slower                                      |
| unpickle                   | 14.9 us                                                | 15.4 us: 1.03x slower                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.03x slower                                     |
| pidigits                   | 186 ms                                                 | 194 ms: 1.04x slower                                       |
| asyncio_tcp                | 488 ms                                                 | 511 ms: 1.05x slower                                       |
| mdp                        | 2.74 sec                                               | 2.89 sec: 1.05x slower                                     |
| python_startup             | 10.6 ms                                                | 11.1 ms: 1.05x slower                                      |
| unpickle_list              | 4.96 us                                                | 5.26 us: 1.06x slower                                      |
| pycparser                  | 1.19 sec                                               | 1.27 sec: 1.07x slower                                     |
| richards                   | 48.1 ms                                                | 51.9 ms: 1.08x slower                                      |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.08x slower                                      |
| generators                 | 28.8 ms                                                | 31.2 ms: 1.08x slower                                      |
| genshi_text                | 22.9 ms                                                | 24.9 ms: 1.09x slower                                      |
| richards_super             | 54.4 ms                                                | 59.1 ms: 1.09x slower                                      |
| meteor_contest             | 108 ms                                                 | 117 ms: 1.09x slower                                       |
| pylint                     | 313 ms                                                 | 341 ms: 1.09x slower                                       |
| pprint_safe_repr           | 744 ms                                                 | 812 ms: 1.09x slower                                       |
| json                       | 5.20 ms                                                | 5.68 ms: 1.09x slower                                      |
| aiohttp                    | 1.14 ms                                                | 1.25 ms: 1.09x slower                                      |
| gunicorn                   | 1.23 ms                                                | 1.35 ms: 1.10x slower                                      |
| crypto_pyaes               | 73.0 ms                                                | 80.1 ms: 1.10x slower                                      |
| nqueens                    | 80.6 ms                                                | 88.6 ms: 1.10x slower                                      |
| scimark_fft                | 369 ms                                                 | 405 ms: 1.10x slower                                       |
| sqlglot_normalize          | 107 ms                                                 | 118 ms: 1.10x slower                                       |
| pprint_pformat             | 1.51 sec                                               | 1.66 sec: 1.10x slower                                     |
| scimark_lu                 | 115 ms                                                 | 126 ms: 1.10x slower                                       |
| coroutines                 | 22.5 ms                                                | 24.8 ms: 1.10x slower                                      |
| sqlglot_optimize           | 53.9 ms                                                | 59.4 ms: 1.10x slower                                      |
| go                         | 142 ms                                                 | 157 ms: 1.11x slower                                       |
| 2to3                       | 265 ms                                                 | 294 ms: 1.11x slower                                       |
| pyflate                    | 460 ms                                                 | 510 ms: 1.11x slower                                       |
| html5lib                   | 64.5 ms                                                | 71.7 ms: 1.11x slower                                      |
| deepcopy                   | 352 us                                                 | 392 us: 1.11x slower                                       |
| django_template            | 34.4 ms                                                | 38.3 ms: 1.11x slower                                      |
| deepcopy_reduce            | 3.17 us                                                | 3.53 us: 1.11x slower                                      |
| genshi_xml                 | 50.3 ms                                                | 56.2 ms: 1.12x slower                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.61 ms: 1.12x slower                                      |
| pickle_pure_python         | 300 us                                                 | 335 us: 1.12x slower                                       |
| docutils                   | 2.58 sec                                               | 2.89 sec: 1.12x slower                                     |
| flaskblogging              | 9.11 ms                                                | 10.2 ms: 1.12x slower                                      |
| tomli_loads                | 2.11 sec                                               | 2.37 sec: 1.12x slower                                     |
| hexiom                     | 6.13 ms                                                | 6.86 ms: 1.12x slower                                      |
| xml_etree_iterparse        | 102 ms                                                 | 114 ms: 1.12x slower                                       |
| dulwich_log                | 63.0 ms                                                | 70.8 ms: 1.12x slower                                      |
| comprehensions             | 16.4 us                                                | 18.5 us: 1.13x slower                                      |
| spectral_norm              | 115 ms                                                 | 130 ms: 1.13x slower                                       |
| deepcopy_memo              | 38.0 us                                                | 43.0 us: 1.13x slower                                      |
| sqlite_synth               | 2.85 us                                                | 3.23 us: 1.13x slower                                      |
| chameleon                  | 6.85 ms                                                | 7.76 ms: 1.13x slower                                      |
| logging_format             | 6.25 us                                                | 7.09 us: 1.13x slower                                      |
| logging_silent             | 102 ns                                                 | 116 ns: 1.14x slower                                       |
| telco                      | 8.45 ms                                                | 9.60 ms: 1.14x slower                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.44 ms: 1.14x slower                                      |
| logging_simple             | 5.66 us                                                | 6.44 us: 1.14x slower                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.79 ms: 1.14x slower                                      |
| regex_compile              | 131 ms                                                 | 149 ms: 1.14x slower                                       |
| scimark_sor                | 122 ms                                                 | 140 ms: 1.14x slower                                       |
| json_loads                 | 27.0 us                                                | 30.9 us: 1.15x slower                                      |
| scimark_monte_carlo        | 66.3 ms                                                | 76.1 ms: 1.15x slower                                      |
| unpickle_pure_python       | 213 us                                                 | 246 us: 1.15x slower                                       |
| sympy_integrate            | 19.9 ms                                                | 22.9 ms: 1.15x slower                                      |
| async_generators           | 433 ms                                                 | 500 ms: 1.15x slower                                       |
| pathlib                    | 17.1 ms                                                | 19.8 ms: 1.16x slower                                      |
| mako                       | 11.1 ms                                                | 12.9 ms: 1.17x slower                                      |
| chaos                      | 58.4 ms                                                | 68.7 ms: 1.18x slower                                      |
| tornado_http               | 91.5 ms                                                | 108 ms: 1.18x slower                                       |
| fannkuch                   | 381 ms                                                 | 451 ms: 1.18x slower                                       |
| raytrace                   | 262 ms                                                 | 314 ms: 1.20x slower                                       |
| sympy_str                  | 274 ms                                                 | 332 ms: 1.21x slower                                       |
| float                      | 78.5 ms                                                | 95.5 ms: 1.22x slower                                      |
| deltablue                  | 3.15 ms                                                | 3.99 ms: 1.27x slower                                      |
| nbody                      | 85.7 ms                                                | 110 ms: 1.28x slower                                       |
| sympy_expand               | 462 ms                                                 | 613 ms: 1.33x slower                                       |
| bench_thread_pool          | 815 us                                                 | 1.09 ms: 1.33x slower                                      |
| python_startup_no_site     | 6.99 ms                                                | 9.60 ms: 1.37x slower                                      |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 804 ms: 1.40x slower                                       |
| sympy_sum                  | 150 ms                                                 | 211 ms: 1.41x slower                                       |
| async_tree_none            | 354 ms                                                 | 509 ms: 1.44x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 657 ms: 1.48x slower                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 692 ms: 1.49x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 850 ms: 1.56x slower                                       |
| async_tree_io              | 843 ms                                                 | 1.39 sec: 1.65x slower                                     |
| async_tree_none_tg         | 320 ms                                                 | 540 ms: 1.69x slower                                       |
| async_tree_io_tg           | 825 ms                                                 | 1.45 sec: 1.76x slower                                     |
| xml_etree_parse            | 156 ms                                                 | 472 ms: 3.03x slower                                       |
| coverage                   | 83.7 ms                                                | 725 ms: 8.66x slower                                       |
| thrift                     | 796 us                                                 | 9.50 ms: 11.93x slower                                     |
| xml_etree_process          | 60.4 ms                                                | 1.03 sec: 17.03x slower                                    |
| xml_etree_generate         | 87.0 ms                                                | 1.58 sec: 18.18x slower                                    |
| Geometric mean             | (ref)                                                  | 1.27x slower                                               |

Benchmark hidden because not significant (1): mypy2
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, dask, djangocms, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.11x

# Memory
- memory change: 0.58x