# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_mprotect
- machine: darwin-arm64
- commit hash: e6d8e6d
- commit date: 2024-03-15
- overall geometric mean: 1.04x slower
- HPT reliability: 99.83%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.43x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 183 ms: 1.08x slower                                                    |
| chameleon      | 4.70 ms                                                | 4.84 ms: 1.03x slower                                                   |
| docutils       | 1.50 sec                                               | 1.52 sec: 1.01x slower                                                  |
| tornado_http   | 69.3 ms                                                | 83.7 ms: 1.21x slower                                                   |
| Geometric mean | (ref)                                                  | 1.08x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none        | 266 ms                                                 | 253 ms: 1.05x faster                                                    |
| async_tree_io_tg       | 669 ms                                                 | 673 ms: 1.01x slower                                                    |
| async_tree_none_tg     | 258 ms                                                 | 261 ms: 1.01x slower                                                    |
| async_tree_memoization | 312 ms                                                 | 330 ms: 1.06x slower                                                    |
| async_tree_io          | 668 ms                                                 | 706 ms: 1.06x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                            |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 53.0 ms: 1.05x faster                                                   |
| pidigits       | 282 ms                                                 | 282 ms: 1.00x slower                                                    |
| nbody          | 68.8 ms                                                | 70.4 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 153 ms: 1.01x faster                                                    |
| regex_effbot   | 2.64 ms                                                | 2.63 ms: 1.01x faster                                                   |
| regex_v8       | 16.0 ms                                                | 17.3 ms: 1.08x slower                                                   |
| regex_compile  | 77.9 ms                                                | 85.2 ms: 1.09x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 1.39 sec                                               | 1.33 sec: 1.05x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 38.8 ms: 1.02x faster                                                   |
| pickle_pure_python   | 200 us                                                 | 198 us: 1.01x faster                                                    |
| json_loads           | 17.2 us                                                | 17.1 us: 1.01x faster                                                   |
| unpickle_pure_python | 151 us                                                 | 150 us: 1.00x faster                                                    |
| xml_etree_generate   | 55.8 ms                                                | 55.8 ms: 1.00x faster                                                   |
| pickle_dict          | 18.1 us                                                | 18.1 us: 1.00x slower                                                   |
| unpickle             | 9.12 us                                                | 9.18 us: 1.01x slower                                                   |
| xml_etree_iterparse  | 74.0 ms                                                | 74.9 ms: 1.01x slower                                                   |
| unpickle_list        | 3.02 us                                                | 3.11 us: 1.03x slower                                                   |
| pickle_list          | 2.89 us                                                | 2.99 us: 1.03x slower                                                   |
| json_dumps           | 6.22 ms                                                | 6.49 ms: 1.04x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_parse, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 16.8 ms: 1.47x slower                                                   |
| python_startup_no_site | 9.37 ms                                                | 15.2 ms: 1.62x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.54x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.72 ms: 1.15x faster                                                   |
| django_template | 22.3 ms                                                | 21.9 ms: 1.02x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 93.0 us                                                | 72.0 us: 1.29x faster                                                   |
| comprehensions           | 14.5 us                                                | 12.5 us: 1.16x faster                                                   |
| mako                     | 7.71 ms                                                | 6.72 ms: 1.15x faster                                                   |
| raytrace                 | 212 ms                                                 | 190 ms: 1.11x faster                                                    |
| asyncio_tcp              | 449 ms                                                 | 408 ms: 1.10x faster                                                    |
| crypto_pyaes             | 51.9 ms                                                | 47.4 ms: 1.10x faster                                                   |
| generators               | 31.1 ms                                                | 28.5 ms: 1.09x faster                                                   |
| deltablue                | 2.71 ms                                                | 2.53 ms: 1.07x faster                                                   |
| logging_simple           | 3.69 us                                                | 3.45 us: 1.07x faster                                                   |
| logging_format           | 3.98 us                                                | 3.76 us: 1.06x faster                                                   |
| chaos                    | 42.5 ms                                                | 40.1 ms: 1.06x faster                                                   |
| logging_silent           | 76.4 ns                                                | 72.2 ns: 1.06x faster                                                   |
| deepcopy_memo            | 27.7 us                                                | 26.2 us: 1.05x faster                                                   |
| float                    | 55.8 ms                                                | 53.0 ms: 1.05x faster                                                   |
| deepcopy_reduce          | 2.07 us                                                | 1.97 us: 1.05x faster                                                   |
| async_tree_none          | 266 ms                                                 | 253 ms: 1.05x faster                                                    |
| coroutines               | 19.2 ms                                                | 18.3 ms: 1.05x faster                                                   |
| tomli_loads              | 1.39 sec                                               | 1.33 sec: 1.05x faster                                                  |
| json                     | 3.09 ms                                                | 2.96 ms: 1.04x faster                                                   |
| sqlglot_parse            | 848 us                                                 | 814 us: 1.04x faster                                                    |
| deepcopy                 | 235 us                                                 | 229 us: 1.03x faster                                                    |
| spectral_norm            | 76.4 ms                                                | 74.7 ms: 1.02x faster                                                   |
| django_template          | 22.3 ms                                                | 21.9 ms: 1.02x faster                                                   |
| sympy_str                | 148 ms                                                 | 144 ms: 1.02x faster                                                    |
| xml_etree_process        | 39.7 ms                                                | 38.8 ms: 1.02x faster                                                   |
| sqlglot_transpile        | 1.02 ms                                                | 1.00 ms: 1.02x faster                                                   |
| sqlglot_normalize        | 186 ms                                                 | 183 ms: 1.02x faster                                                    |
| pickle_pure_python       | 200 us                                                 | 198 us: 1.01x faster                                                    |
| regex_dna                | 154 ms                                                 | 153 ms: 1.01x faster                                                    |
| json_loads               | 17.2 us                                                | 17.1 us: 1.01x faster                                                   |
| regex_effbot             | 2.64 ms                                                | 2.63 ms: 1.01x faster                                                   |
| scimark_monte_carlo      | 45.0 ms                                                | 44.9 ms: 1.00x faster                                                   |
| scimark_sparse_mat_mult  | 3.14 ms                                                | 3.13 ms: 1.00x faster                                                   |
| unpickle_pure_python     | 151 us                                                 | 150 us: 1.00x faster                                                    |
| asyncio_websockets       | 409 ms                                                 | 409 ms: 1.00x faster                                                    |
| xml_etree_generate       | 55.8 ms                                                | 55.8 ms: 1.00x faster                                                   |
| pidigits                 | 282 ms                                                 | 282 ms: 1.00x slower                                                    |
| pickle_dict              | 18.1 us                                                | 18.1 us: 1.00x slower                                                   |
| gc_traversal             | 2.40 ms                                                | 2.41 ms: 1.01x slower                                                   |
| async_tree_io_tg         | 669 ms                                                 | 673 ms: 1.01x slower                                                    |
| unpickle                 | 9.12 us                                                | 9.18 us: 1.01x slower                                                   |
| xml_etree_iterparse      | 74.0 ms                                                | 74.9 ms: 1.01x slower                                                   |
| async_tree_none_tg       | 258 ms                                                 | 261 ms: 1.01x slower                                                    |
| pprint_safe_repr         | 497 ms                                                 | 504 ms: 1.01x slower                                                    |
| sqlite_synth             | 1.57 us                                                | 1.59 us: 1.01x slower                                                   |
| docutils                 | 1.50 sec                                               | 1.52 sec: 1.01x slower                                                  |
| mdp                      | 1.58 sec                                               | 1.61 sec: 1.02x slower                                                  |
| bench_thread_pool        | 504 us                                                 | 513 us: 1.02x slower                                                    |
| create_gc_cycles         | 701 us                                                 | 714 us: 1.02x slower                                                    |
| scimark_fft              | 195 ms                                                 | 199 ms: 1.02x slower                                                    |
| nqueens                  | 62.4 ms                                                | 63.8 ms: 1.02x slower                                                   |
| nbody                    | 68.8 ms                                                | 70.4 ms: 1.02x slower                                                   |
| async_generators         | 304 ms                                                 | 311 ms: 1.02x slower                                                    |
| dask                     | 222 ms                                                 | 227 ms: 1.02x slower                                                    |
| dulwich_log              | 29.8 ms                                                | 30.6 ms: 1.03x slower                                                   |
| pprint_pformat           | 1.01 sec                                               | 1.04 sec: 1.03x slower                                                  |
| richards_super           | 36.0 ms                                                | 37.1 ms: 1.03x slower                                                   |
| sympy_expand             | 241 ms                                                 | 248 ms: 1.03x slower                                                    |
| sqlglot_optimize         | 34.0 ms                                                | 35.0 ms: 1.03x slower                                                   |
| unpickle_list            | 3.02 us                                                | 3.11 us: 1.03x slower                                                   |
| chameleon                | 4.70 ms                                                | 4.84 ms: 1.03x slower                                                   |
| fannkuch                 | 248 ms                                                 | 256 ms: 1.03x slower                                                    |
| pathlib                  | 24.2 ms                                                | 25.1 ms: 1.03x slower                                                   |
| pickle_list              | 2.89 us                                                | 2.99 us: 1.03x slower                                                   |
| aiohttp                  | 1.08 ms                                                | 1.12 ms: 1.04x slower                                                   |
| richards                 | 32.1 ms                                                | 33.3 ms: 1.04x slower                                                   |
| meteor_contest           | 71.7 ms                                                | 74.7 ms: 1.04x slower                                                   |
| json_dumps               | 6.22 ms                                                | 6.49 ms: 1.04x slower                                                   |
| pyflate                  | 316 ms                                                 | 331 ms: 1.05x slower                                                    |
| asyncio_tcp_ssl          | 1.24 sec                                               | 1.31 sec: 1.05x slower                                                  |
| async_tree_memoization   | 312 ms                                                 | 330 ms: 1.06x slower                                                    |
| async_tree_io            | 668 ms                                                 | 706 ms: 1.06x slower                                                    |
| pycparser                | 677 ms                                                 | 717 ms: 1.06x slower                                                    |
| 2to3                     | 169 ms                                                 | 183 ms: 1.08x slower                                                    |
| regex_v8                 | 16.0 ms                                                | 17.3 ms: 1.08x slower                                                   |
| go                       | 102 ms                                                 | 110 ms: 1.08x slower                                                    |
| hexiom                   | 4.54 ms                                                | 4.97 ms: 1.09x slower                                                   |
| regex_compile            | 77.9 ms                                                | 85.2 ms: 1.09x slower                                                   |
| scimark_lu               | 76.0 ms                                                | 84.9 ms: 1.12x slower                                                   |
| bench_mp_pool            | 44.9 ms                                                | 51.3 ms: 1.14x slower                                                   |
| tornado_http             | 69.3 ms                                                | 83.7 ms: 1.21x slower                                                   |
| telco                    | 3.68 ms                                                | 4.49 ms: 1.22x slower                                                   |
| coverage                 | 38.9 ms                                                | 48.9 ms: 1.26x slower                                                   |
| scimark_sor              | 87.4 ms                                                | 111 ms: 1.27x slower                                                    |
| python_startup           | 11.4 ms                                                | 16.8 ms: 1.47x slower                                                   |
| python_startup_no_site   | 9.37 ms                                                | 15.2 ms: 1.62x slower                                                   |
| mypy2                    | 380 ms                                                 | 619 ms: 1.63x slower                                                    |
| unpack_sequence          | 31.5 ns                                                | 114 ns: 3.61x slower                                                    |
| Geometric mean           | (ref)                                                  | 1.04x slower                                                            |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, xml_etree_parse, sympy_sum, async_tree_cpu_io_mixed_tg, pickle, async_tree_memoization_tg, sympy_integrate, gunicorn
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240315-3.13.0a5+-e6d8e6d-JIT/bm-20240315-darwin-arm64-brandtbucher-justin_mprotect-3.13.0a5+-e6d8e6d.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 99.83% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.43x