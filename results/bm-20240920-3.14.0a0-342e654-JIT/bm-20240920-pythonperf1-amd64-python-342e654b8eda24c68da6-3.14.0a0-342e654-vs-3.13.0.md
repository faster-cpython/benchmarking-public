# Results vs. 3.13.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: windows-amd64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.030x faster
- HPT reliability: 97.59%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 241 ms: 1.09x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.92 sec: 1.22x slower                                                     |
| html5lib       | 38.9 ms                                                     | 41.9 ms: 1.08x slower                                                      |
| tornado_http   | 93.0 ms                                                     | 87.6 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                       | 1.08x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 256 ms: 1.13x faster                                                       |
| async_tree_none            | 226 ms                                                      | 206 ms: 1.10x faster                                                       |
| async_tree_memoization     | 276 ms                                                      | 260 ms: 1.06x faster                                                       |
| async_tree_none_tg         | 209 ms                                                      | 198 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 395 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 397 ms: 1.05x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 562 ms: 1.08x slower                                                       |
| async_tree_io              | 521 ms                                                      | 584 ms: 1.12x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.6 ms: 1.14x slower                                                      |
| async_generators           | 223 ms                                                      | 261 ms: 1.17x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 68.4 ms                                                     | 49.5 ms: 1.38x faster                                                      |
| float          | 49.9 ms                                                     | 44.3 ms: 1.13x faster                                                      |
| pidigits       | 148 ms                                                      | 149 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 16.1 ms: 1.33x faster                                                      |
| regex_effbot   | 1.58 ms                                                     | 1.55 ms: 1.02x faster                                                      |
| regex_dna      | 115 ms                                                      | 116 ms: 1.00x slower                                                       |
| regex_compile  | 80.5 ms                                                     | 95.0 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                                    | 1.27 sec: 1.09x faster                                                     |
| xml_etree_generate   | 54.0 ms                                                     | 49.4 ms: 1.09x faster                                                      |
| xml_etree_process    | 37.0 ms                                                     | 35.4 ms: 1.05x faster                                                      |
| json_loads           | 15.1 us                                                     | 14.5 us: 1.04x faster                                                      |
| xml_etree_iterparse  | 61.8 ms                                                     | 60.9 ms: 1.02x faster                                                      |
| json_dumps           | 5.92 ms                                                     | 5.87 ms: 1.01x faster                                                      |
| pickle_pure_python   | 190 us                                                      | 191 us: 1.01x slower                                                       |
| unpickle_pure_python | 133 us                                                      | 142 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                               |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 22.1 ms: 1.15x faster                                                      |
| Geometric mean | (ref)                                                       | 1.07x faster                                                               |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.35 ms                                                     | 5.21 ms: 1.22x faster                                                      |
| django_template | 22.4 ms                                                     | 26.9 ms: 1.20x slower                                                      |
| genshi_text     | 15.6 ms                                                     | 18.8 ms: 1.21x slower                                                      |
| genshi_xml      | 35.5 ms                                                     | 44.1 ms: 1.24x slower                                                      |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 513 us: 17.14x faster                                                      |
| deepcopy_memo              | 23.3 us                                                     | 15.5 us: 1.50x faster                                                      |
| spectral_norm              | 62.8 ms                                                     | 44.1 ms: 1.42x faster                                                      |
| create_gc_cycles           | 1.26 ms                                                     | 899 us: 1.40x faster                                                       |
| nbody                      | 68.4 ms                                                     | 49.5 ms: 1.38x faster                                                      |
| regex_v8                   | 21.4 ms                                                     | 16.1 ms: 1.33x faster                                                      |
| gc_traversal               | 1.97 ms                                                     | 1.54 ms: 1.28x faster                                                      |
| scimark_sor                | 76.2 ms                                                     | 61.2 ms: 1.25x faster                                                      |
| deepcopy                   | 226 us                                                      | 184 us: 1.23x faster                                                       |
| mako                       | 6.35 ms                                                     | 5.21 ms: 1.22x faster                                                      |
| bench_mp_pool              | 86.4 ms                                                     | 71.7 ms: 1.21x faster                                                      |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.09 ms: 1.18x faster                                                      |
| crypto_pyaes               | 45.4 ms                                                     | 38.7 ms: 1.17x faster                                                      |
| scimark_fft                | 172 ms                                                      | 150 ms: 1.15x faster                                                       |
| python_startup             | 25.4 ms                                                     | 22.1 ms: 1.15x faster                                                      |
| float                      | 49.9 ms                                                     | 44.3 ms: 1.13x faster                                                      |
| async_tree_memoization_tg  | 288 ms                                                      | 256 ms: 1.13x faster                                                       |
| async_tree_none            | 226 ms                                                      | 206 ms: 1.10x faster                                                       |
| tomli_loads                | 1.39 sec                                                    | 1.27 sec: 1.09x faster                                                     |
| deepcopy_reduce            | 2.06 us                                                     | 1.88 us: 1.09x faster                                                      |
| xml_etree_generate         | 54.0 ms                                                     | 49.4 ms: 1.09x faster                                                      |
| json                       | 3.19 ms                                                     | 2.94 ms: 1.09x faster                                                      |
| pyflate                    | 283 ms                                                      | 265 ms: 1.07x faster                                                       |
| fannkuch                   | 253 ms                                                      | 238 ms: 1.07x faster                                                       |
| pathlib                    | 80.9 ms                                                     | 76.1 ms: 1.06x faster                                                      |
| deltablue                  | 1.92 ms                                                     | 1.81 ms: 1.06x faster                                                      |
| tornado_http               | 93.0 ms                                                     | 87.6 ms: 1.06x faster                                                      |
| async_tree_memoization     | 276 ms                                                      | 260 ms: 1.06x faster                                                       |
| async_tree_none_tg         | 209 ms                                                      | 198 ms: 1.06x faster                                                       |
| bench_thread_pool          | 847 us                                                      | 803 us: 1.05x faster                                                       |
| xml_etree_process          | 37.0 ms                                                     | 35.4 ms: 1.05x faster                                                      |
| json_loads                 | 15.1 us                                                     | 14.5 us: 1.04x faster                                                      |
| xml_etree_iterparse        | 61.8 ms                                                     | 60.9 ms: 1.02x faster                                                      |
| regex_effbot               | 1.58 ms                                                     | 1.55 ms: 1.02x faster                                                      |
| telco                      | 4.79 ms                                                     | 4.73 ms: 1.01x faster                                                      |
| json_dumps                 | 5.92 ms                                                     | 5.87 ms: 1.01x faster                                                      |
| regex_dna                  | 115 ms                                                      | 116 ms: 1.00x slower                                                       |
| pickle_pure_python         | 190 us                                                      | 191 us: 1.01x slower                                                       |
| coverage                   | 45.6 ms                                                     | 46.1 ms: 1.01x slower                                                      |
| pidigits                   | 148 ms                                                      | 149 ms: 1.01x slower                                                       |
| logging_simple             | 5.96 us                                                     | 6.04 us: 1.01x slower                                                      |
| mdp                        | 1.39 sec                                                    | 1.41 sec: 1.02x slower                                                     |
| pprint_safe_repr           | 494 ms                                                      | 503 ms: 1.02x slower                                                       |
| scimark_lu                 | 53.0 ms                                                     | 54.0 ms: 1.02x slower                                                      |
| comprehensions             | 10.3 us                                                     | 10.6 us: 1.03x slower                                                      |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 395 ms: 1.03x slower                                                       |
| chaos                      | 38.5 ms                                                     | 40.0 ms: 1.04x slower                                                      |
| pycparser                  | 683 ms                                                      | 709 ms: 1.04x slower                                                       |
| logging_silent             | 54.6 ns                                                     | 56.7 ns: 1.04x slower                                                      |
| pprint_pformat             | 999 ms                                                      | 1.04 sec: 1.04x slower                                                     |
| logging_format             | 6.26 us                                                     | 6.52 us: 1.04x slower                                                      |
| dulwich_log                | 40.8 ms                                                     | 42.6 ms: 1.04x slower                                                      |
| go                         | 87.0 ms                                                     | 91.3 ms: 1.05x slower                                                      |
| scimark_monte_carlo        | 40.8 ms                                                     | 42.9 ms: 1.05x slower                                                      |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 397 ms: 1.05x slower                                                       |
| unpickle_pure_python       | 133 us                                                      | 142 us: 1.06x slower                                                       |
| html5lib                   | 38.9 ms                                                     | 41.9 ms: 1.08x slower                                                      |
| typing_runtime_protocols   | 105 us                                                      | 114 us: 1.08x slower                                                       |
| async_tree_io_tg           | 518 ms                                                      | 562 ms: 1.08x slower                                                       |
| 2to3                       | 221 ms                                                      | 241 ms: 1.09x slower                                                       |
| nqueens                    | 56.7 ms                                                     | 62.4 ms: 1.10x slower                                                      |
| sympy_str                  | 169 ms                                                      | 188 ms: 1.12x slower                                                       |
| async_tree_io              | 521 ms                                                      | 584 ms: 1.12x slower                                                       |
| sympy_sum                  | 86.9 ms                                                     | 98.3 ms: 1.13x slower                                                      |
| sympy_expand               | 291 ms                                                      | 330 ms: 1.13x slower                                                       |
| sqlglot_parse              | 771 us                                                      | 880 us: 1.14x slower                                                       |
| coroutines                 | 12.8 ms                                                     | 14.6 ms: 1.14x slower                                                      |
| sqlglot_normalize          | 175 ms                                                      | 201 ms: 1.15x slower                                                       |
| async_generators           | 223 ms                                                      | 261 ms: 1.17x slower                                                       |
| regex_compile              | 80.5 ms                                                     | 95.0 ms: 1.18x slower                                                      |
| sympy_integrate            | 12.5 ms                                                     | 14.8 ms: 1.18x slower                                                      |
| generators                 | 19.5 ms                                                     | 23.1 ms: 1.18x slower                                                      |
| sqlglot_transpile          | 956 us                                                      | 1.15 ms: 1.20x slower                                                      |
| django_template            | 22.4 ms                                                     | 26.9 ms: 1.20x slower                                                      |
| genshi_text                | 15.6 ms                                                     | 18.8 ms: 1.21x slower                                                      |
| docutils                   | 1.57 sec                                                    | 1.92 sec: 1.22x slower                                                     |
| sqlglot_optimize           | 32.9 ms                                                     | 40.3 ms: 1.22x slower                                                      |
| raytrace                   | 160 ms                                                      | 197 ms: 1.23x slower                                                       |
| genshi_xml                 | 35.5 ms                                                     | 44.1 ms: 1.24x slower                                                      |
| richards_super             | 30.9 ms                                                     | 38.6 ms: 1.25x slower                                                      |
| hexiom                     | 3.89 ms                                                     | 4.87 ms: 1.25x slower                                                      |
| pylint                     | 211 ms                                                      | 264 ms: 1.25x slower                                                       |
| richards                   | 27.3 ms                                                     | 36.1 ms: 1.32x slower                                                      |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                               |

Benchmark hidden because not significant (3): xml_etree_parse, meteor_contest, python_startup_no_site
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-pythonperf1-amd64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.030x faster
# HPT report

- Reliability score: 97.59% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown